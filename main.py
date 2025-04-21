from gmail_auth import authenticate_gmail
from email_fetcher import fetch_emails
from classifier import classify_email
from gmail_auth import label_email, create_label_if_not_exists

def main():
    service = authenticate_gmail()
    emails = fetch_emails(service)

    label_id = create_label_if_not_exists(service, "Positive Response")

    for email in emails:
        print(f"Checking email: {email['subject']}")
classification = classify_email(email['subject'], email['body'])
        print(f"  ➤ Classified as: {classification}")
        if classification.lower() == "positive update":
            label_email(service, email['id'], label_id)

if __name__ == "__main__":
    main()
