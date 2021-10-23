import os
from dotenv import load_dotenv
from .utils import gmail_service

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def main():
    load_dotenv()
    creds_file = os.environ["NEWSLETTER_CREDS_FILE"]
    token_file = os.environ["NEWSLETTER_TOKEN_FILE"]
    gmail = gmail_service(SCOPES, creds_file, token_file)
    # results = gmail.users().labels().list(userId="me").execute()
    # print(results)
    messages = (
        gmail.users()
        .messages()
        .list(userId="me", labelIds=["Label_366279561083306179"], maxResults=10)
    ).execute()
    for message in messages["messages"]:
        print(message["id"])

    # message = gmail.users().messages().get(userId="me", id="17b63e5c9c10d741").execute()
    # print(message)


if __name__ == "__main__":
    main()
