import imaplib

class GmailClient:
    def __init__(self, user, password, imap_url="imap.gmail.com"):
        self.user = user
        self.password = password
        self.imap_url = imap_url
        self.connection = None

    def connect(self):
        self.connection = imaplib.IMAP4_SSL(self.imap_url)
        self.connection.login(self.user, self.password)

    def disconnect(self):
        if self.connection:
            self.connection.logout()

    def get_email_count_for_folder(self, folder_name):
        if not self.connection:
            raise ValueError("Connection not established. Call connect() first.")
        
        result, data = self.connection.select(folder_name)
        return len(data[0].split())

def main():
    user = "manish.sharma.intimetec@gmail.com"
    password = "uhst ymou sids ifdt"

    gmail_client = GmailClient(user, password)

    try:
        gmail_client.connect()

        standard_emails = gmail_client.get_email_count_for_folder("")
        spam_emails = gmail_client.get_email_count_for_folder("Inbox")

        print("Standard Emails:", standard_emails)
        print("Spam Emails:", spam_emails)

    finally:
        gmail_client.disconnect()

if __name__ == "__main__":
    main()
