import base64
from email import message_from_bytes

def fetch_emails(service, max_results=10):
    results = service.users().messages().list(userId='me', maxResults=max_results).execute()
    messages = results.get('messages', [])

    emails = []
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
        headers = msg_data['payload']['headers']
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(No Subject)')

        parts = msg_data['payload'].get('parts')
        if parts:
            body_data = parts[0]['body'].get('data')
        else:
            body_data = msg_data['payload']['body'].get('data')

        if body_data:
            body_decoded = base64.urlsafe_b64decode(body_data.encode('ASCII'))
            body_text = message_from_bytes(body_decoded).get_payload()
        else:
            body_text = ''

        emails.append({
            'id': msg['id'],
            'subject': subject,
            'body': body_text
        })

    return emails
