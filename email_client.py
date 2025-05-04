import os
import pickle
import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# If modifying scope is necessary (offline access)
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

# Path to token.json (stored refresh token)
TOKEN_PATH = 'token.json'
CREDENTIALS_PATH = 'credentials.json'


def authenticate_gmail():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKEN_PATH, 'wb') as token:
            pickle.dump(creds, token)

    return creds

def fetch_emails():
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials=creds)

    # Fetch latest 10 emails from inbox
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=10).execute()
    messages = results.get('messages', [])

    email_list = []
    for msg in messages:
        msg_detail = service.users().messages().get(userId='me', id=msg['id']).execute()
        subject = ''
        headers = msg_detail.get('payload', {}).get('headers', [])
        for header in headers:
            if header['name'] == 'Subject':
                subject = header['value']
        email_list.append({
            'id': msg['id'],
            'snippet': msg_detail.get('snippet', ''),
            'subject': subject,
            'service': service
        })

    return email_list
