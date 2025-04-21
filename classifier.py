import re

def clean_forwarded_email(body):
    # Remove common forwarded email headers
    body = re.sub(r'^From:.*$', '', body, flags=re.MULTILINE)
    body = re.sub(r'^Sent:.*$', '', body, flags=re.MULTILINE)
    body = re.sub(r'^To:.*$', '', body, flags=re.MULTILINE)
    body = re.sub(r'^Subject:.*$', '', body, flags=re.MULTILINE)
    body = re.sub(r'\n+', '\n', body).strip()
    return body

def classify_email(subject, body, keywords):
    full_text = f"{subject.lower()} {body.lower()}"
    for phrase in keywords['positive_keywords']:
        if phrase in full_text:
            return "Positive Update"
    for phrase in keywords['negative_keywords']:
        if phrase in full_text:
            return "Negative Outcome"
    for phrase in keywords['application_received_keywords']:
        if phrase in full_text:
            return "Application Received"
    return "Uncategorized"
