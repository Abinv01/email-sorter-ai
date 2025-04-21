# test_classifier.py

from classifier import classify_email

# Test cases for positive, negative, neutral, and application received emails
test_emails = [
    {
        "subject": "Congratulations! You've been shortlisted for the next round.",
        "body": "We are excited to inform you that you have moved forward in the interview process.",
        "expected_result": "Positive Update"
    },
    {
        "subject": "Senior Consultant, Product Strategy – 799593 update",
        "body": """Hi Abhinav, Thank you for applying for the position of Senior Consultant, Product Strategy at NAB. 
We appreciate your interest in the role and the time you invested into your application.

We regret to advise that after careful review, we will not be moving forward with your application. This decision was not made lightly and we had many strong candidates to choose from. 
Ultimately, we have selected other applicants whose experience more closely aligns with our current needs.

We encourage you to apply for future openings that match your skills and interests and invite you to follow our career page and LinkedIn profile to stay updated on new opportunities at NAB.

Thank you once again for your interest in NAB and for considering us as a potential employer. We wish you all the best in your job search and future career endeavours.""",
        "expected_result": "Negative Outcome"
    },
    {
        "subject": "Account Registration Confirmation",
        "body": "Thank you for registering. Your account has been successfully created.",
        "expected_result": "Application Received"
    },
    {
        "subject": "Interview Invitation for the next steps",
        "body": "We would like to schedule an interview for the next steps in the hiring process.",
        "expected_result": "Positive Update"
    },
    {
        "subject": "Your Application for the Position Implementation Manager 92015",
        "body": """Hi Abhinav,

Thank you for applying for the Implementation Manager 92015 position. We appreciate the time that you have invested in your application.

We will be in touch to provide you with an update on your application. In the meantime, we encourage you to visit the ANZ Careers site regularly to view current vacancies.

On the ANZ Careers site you can also keep your candidate profile up-to-date; and set up so that you’re automatically emailed any suitable vacancies, ensuring you’re one of the first to hear about exciting new opportunities!

At ANZ, we believe in the inherent strength of a vibrant, diverse and inclusive workplace where the backgrounds, perspectives and life experiences of our people create a great place to belong. To assist you through this recruitment process, we encourage you to let us know if there is any accessibility support or adjustments we can provide you with. 

For example, an Auslan interpreter, wheelchair access to the interview venue, adjustments to testing because of low vision or hearing impairment. Please email us at anz-peopleassist@anz.com with the details of the accessibility support or adjustments you need, or let us know if you prefer someone to call you to discuss further.

Thank you for taking the time to consider ANZ as your next career move. Good luck!

Kind Regards,
ANZ Recruitment Team""",
        "expected_result": "Application Received"
    }
]

# Run the classifier on each test case
for email in test_emails:
    result = classify_email(email["subject"], email["body"])
    print(f"Subject: {email['subject']}\n")
    print(f"Expected Result: {email['expected_result']}")
    print(f"Classified As:    {result}")
    print("-" * 70)
