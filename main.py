import os
import base64
import json
import logging
from email import message_from_bytes
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.json'
KEYWORDS_FILE = 'config/keywords.json'

LABEL_MAP = {
    'positive': 'Positive Update',
    'negative': 'Negative Outcome',
    'application_received': 'Application Received'
}


def load_keywords():
    with open(KEYWORDS_FILE, 'r') as f:
        return json.load(f)


def authenticate():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    return creds


def get_unread_messages(service):
    results = service.users().messages().list(userId='me', labelIds=['UNREAD']).execute()
    return results.get('messages', [])


def get_message_content(service, msg_id):
    msg = service.users().messages().get(userId='me', id=msg_id, format='raw').execute()
    raw_data = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))
    email_message = message_from_bytes(raw_data)
    subject = email_message.get('Subject', '')
    payload = email_message.get_payload()
    body = ""
    if isinstance(payload, list):
        for part in payload:
            if part.get_content_type() == 'text/plain':
                body += part.get_payload(decode=True).decode(errors='ignore')
    elif isinstance(payload, str):
        body = payload
    return subject.lower(), body.lower()


def create_label_if_not_exists(service, label_name):
    labels = service.users().labels().list(userId='me').execute().get('labels', [])
    for label in labels:
        if label['name'].lower() == label_name.lower():
            return label['id']

    label_obj = {
        'name': label_name,
        'labelListVisibility': 'labelShow',
        'messageListVisibility': 'show'
    }
    new_label = service.users().labels().create(userId='me', body=label_obj).execute()
    logging.info(f"Created label '{label_name}'")
    return new_label['id']


def classify_email(subject, body, keywords):
    for keyword in keywords['positive_keywords']:
        if keyword in subject or keyword in body:
            return 'positive'
    for keyword in keywords['negative_keywords']:
        if keyword in subject or keyword in body:
            return 'negative'
    for keyword in keywords['application_received_keywords']:
        if keyword in subject or keyword in body:
            return 'application_received'
    return None


def main():
    logging.info("Starting email classification script...")

    creds = authenticate()
    service = build('gmail', 'v1', credentials=creds)
    keywords = load_keywords()

    # Ensure labels exist and map them
    label_ids = {}
    for category, label_name in LABEL_MAP.items():
        label_ids[category] = create_label_if_not_exists(service, label_name)

    messages = get_unread_messages(service)
    logging.info(f"Found {len(messages)} unread emails")

    for msg in messages:
        msg_id = msg['id']
        try:
            subject, body = get_message_content(service, msg_id)
            classification = classify_email(subject, body, keywords)

            if classification:
                label_id = label_ids[classification]
                service.users().messages().modify(
                    userId='me', id=msg_id,
                    body={
                        'addLabelIds': [label_id],
                        'removeLabelIds': ['INBOX'] if classification != 'positive' else []
                    }
                ).execute()
                logging.info(f"Labeled message {msg_id} as '{LABEL_MAP[classification]}'")
            else:
                logging.info(f"No classification match for email {msg_id}")

        except Exception as e:
            logging.error(f"Failed to process message {msg_id}: {e}")

    logging.info("Email processing completed.")


if __name__ == '__main__':
    main()
