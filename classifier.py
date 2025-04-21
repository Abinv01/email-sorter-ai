# classifier.py

import json

CONFIG_FILE = "keywords_config.json"

def load_keywords():
    with open(CONFIG_FILE, "r") as file:
        data = json.load(file)
        print("Loaded keywords:", data)  # Debugging line to show the contents
        return data

keywords = load_keywords()

def classify_email(subject, body):
    content = f"{subject.lower()} {body.lower()}"

    # Handle negative outcome emails (e.g., rejection)
    for phrase in keywords.get("negative_keywords", []):  # Corrected key
        if phrase in content:
            return "Negative Response"

    # Handle application received emails
    for phrase in keywords.get("application_received_keywords", []):  # Corrected key
        if phrase in content:
            return "Application Received"

    # Handle positive outcome emails
    for phrase in keywords.get("positive_keywords", []):  # Corrected key
        if phrase in content:
            return "Positive Update"

    return "Neutral / Unknown"
