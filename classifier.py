import re

def classify_email(text):
    """
    A simple rule-based classifier to determine if an email is a positive job update
    or a rejection email.
    """

    text_lower = text.lower()

    positive_keywords = [
        "next steps", "interview", "shortlisted", "progressing", "moving forward",
        "schedule", "congratulations", "we would like to", "we're impressed"
    ]

    negative_keywords = [
        "unfortunately", "not selected", "regret to inform", "another candidate",
        "unsuccessful", "did not move", "decline"
    ]

    # Check for positive keywords
    for phrase in positive_keywords:
        if phrase in text_lower:
            return "Positive Update"

    # Check for negative keywords
    for phrase in negative_keywords:
        if phrase in text_lower:
            return "Negative Outcome"

    # Default fallback
    return "Neutral / Unknown"
