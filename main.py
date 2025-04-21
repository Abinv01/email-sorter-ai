import json
from email_client import fetch_emails, archive_email
from email_classifier import classify_email, clean_forwarded_email

def load_keywords():
    with open("config/keywords.json", "r") as file:
        return json.load(file)

def main():
    keywords = load_keywords()
    print("Loaded keywords:", keywords)

    emails = fetch_emails()
    for email in emails:
        print(f"\nChecking email: {email['subject']}")
        cleaned_body = clean_forwarded_email(email['body'])
        classification = classify_email(email['subject'], cleaned_body, keywords)
        print(f"  ➤ Classified as: {classification}")

        # Auto-archive logic
        if classification in ['Application Received', 'Negative Outcome']:
            archive_email(email['id'])
            print("  ➤ Archived this email to protect your mental peace ❤️‍🩹")

if __name__ == "__main__":
    main()
