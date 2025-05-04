import re

def clean_forwarded_email(body):
    # Remove common forwarded email headers
    body = re.sub(r'^From:.*$', '', body, flags=re.MULTILINE)
    body = re.sub(r'^Sent:.*$', '', body, flags=re.MULTILINE)
    body = re.sub(r'^To:.*$', '', body, flags=re.MULTILINE)
    body = re.sub(r'^Subject:.*$', '', body, flags=re.MULTILINE)
    body = re.sub(r'\n+', '\n', body).strip()
    print(f"🧹 Cleaned email body: {body}")  # Debugging
    return body

def classify_email(subject, body, keywords):
    full_text = f"{subject.lower()} {body.lower()}"
    print(f"🔍 Checking full text: {full_text}")  # Debugging

    for phrase in keywords['positive_keywords']:
        if phrase in full_text:
            print(f"✔️ Matched positive keyword: {phrase}")  # Debugging
            return "Positive Update"
    for phrase in keywords['negative_keywords']:
        if phrase in full_text:
            print(f"✔️ Matched negative keyword: {phrase}")  # Debugging
            return "Negative Outcome"
    for phrase in keywords['application_received_keywords']:
        if phrase in full_text:
            print(f"✔️ Matched application received keyword: {phrase}")  # Debugging
            return "Application Received"
    print("❌ No match found.")  # Debugging
    return "Uncategorized"

