from classifier import classify_email, load_keywords
from email_client import fetch_emails

def main():
    keywords = load_keywords()
    print("Loaded keywords:", keywords)
    
    emails = fetch_emails()
    
    for email in emails:
        print(f"Checking email: {email['subject']}")
        classification = classify_email(email['subject'], email['body'])
        print(f"  ➤ Classified as: {classification}")

if __name__ == "__main__":
    main()
