import time
from email_client import fetch_emails
from email_classifier import classify_email, clean_forwarded_email
from utils import load_keywords

def main_loop():
    keywords = load_keywords()
    while True:
        print("🔄 Checking for new emails...")
        emails = fetch_emails()
        for email in emails:
            cleaned_body = clean_forwarded_email(email['snippet'])
            classification = classify_email(cleaned_body, keywords)
            print(f"📧 {email['subject']}")
            print(f"  ➤ Classified as: {classification}")

            # Archive based on classification
            if classification in ['Application Received', 'Negative Outcome']:
                print("🗂️ Archiving email...")
                email['service'].users().messages().modify(
                    userId='me',
                    id=email['id'],
                    body={'removeLabelIds': ['INBOX']}
                ).execute()
        print("✅ Done. Sleeping for 5 minutes.\n")
        time.sleep(300)  # 5 minutes

if __name__ == "__main__":
    main_loop()
