

 Email Sorter AI Agent

 ## Overview

The **Email Sorter AI Agent** is a Python-based AI tool that automatically classifies and labels incoming emails based on predefined keywords. It uses the Gmail API to access the user's inbox, classify emails into categories (e.g., "Positive Response", "Negative Outcome", and "Application Received"), and apply labels for better email organization.

The goal of the AI agent is to streamline the process of managing email inboxes, making it easier to focus on important emails and discard irrelevant ones. 

Phase 1: Currently it classfies emails based on keyword match.

Phase 2: In Phase 2 the Agent shall run on an infinite loop with a sleep of 5 minutes and it shall utilise LLM to find patterns and categorise emails based on enhanced capabilities. Phase 2 is currently under testing and will be available soon.

## Features

* Automatically classifies emails based on keyword matches.
* Uses Gmail API to access and modify labels in Gmail.
* Categorizes emails into the following categories:

  * **Positive Response**: Emails that indicate positive feedback, such as interviews, offers, or further steps.
  * **Negative Outcome**: Emails that indicate rejection or unsuccessful application results.
  * **Application Received**: Emails confirming the receipt of job applications.
* Runs indefinitely in an infinite loop, checking for new emails every 5 minutes.

## Prerequisites

Before running the email sorter AI agent, ensure the following:

* **Python 3.x** installed.
* **Google Cloud Console** project setup with Gmail API enabled.
* **OAuth 2.0 credentials** (`credentials.json`) and **OAuth token** (`token.pickle`) generated for your Gmail account.

You can follow the [Google Gmail API Python Quickstart guide](https://developers.google.com/gmail/api/quickstart) to get started with Google Cloud Console and OAuth setup.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Abinv01/email-sorter-ai.git
   cd email-sorter-ai
   ```

2. **Install dependencies**:

   It's recommended to use a virtual environment for Python projects.

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

   Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up credentials**:

   Download your `credentials.json` file from the Google Cloud Console and place it in the root directory of the project.

4. **Run the agent**:

   Run the `main.py` script to start the email sorting process. The script will ask for authorization to access your Gmail account.

   ```bash
   python main.py
   ```

   Follow the on-screen instructions to authorize the app.

## Usage

Once the script is running, it will:

* Access the inbox using the Gmail API.
* Check for new emails every 5 minutes.
* Classify emails based on the keywords specified in `keywords.json`:

  * **Positive Response**: Any email containing keywords related to positive feedback (e.g., "offer", "interview").
  * **Negative Outcome**: Emails containing rejection-related keywords (e.g., "unsuccessful", "not selected").
  * **Application Received**: Emails confirming the receipt of job applications (e.g., "application received", "thank you for applying").
* Move emails to the appropriate labels within Gmail.

You can modify the keywords for classification by updating the `keywords.json` file.

## Configuration

* **keywords.json**: This file contains three categories of keywords: `positive_keywords`, `negative_keywords`, and `application_received_keywords`. You can modify these lists as per your needs.

```json
{
  "positive_keywords": ["interview", "offer", "shortlisted", "congratulations"],
  "negative_keywords": ["unsuccessful", "regret", "decline"],
  "application_received_keywords": ["application received", "thank you for applying"]
}
```

## Troubleshooting

1. **Invalid Credentials**: If the credentials file (`credentials.json`) is not found or is incorrectly configured, the agent will ask you to reauthorize access.

2. **API Quotas**: The Gmail API has usage limits, and you may encounter rate limiting if the agent makes too many requests in a short period. Refer to the [Gmail API Quotas](https://developers.google.com/gmail/api/guides/push) for more information.

3. **No Labels Created**: Ensure that the Gmail account has labels that match the ones specified in the code. Labels are automatically created if they don’t exist.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
