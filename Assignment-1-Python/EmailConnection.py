import imaplib

class EmailConnection:
    def __init__(self):
        self.user = "manish.sharma.intimetec@gmail.com"
        self.password = "uhst ymou sids ifdt"
        self.imapURL = "imap.gmail.com"

    def makeConnectionWithGmailServer(self):
        connectionWithServer = imaplib.IMAP4_SSL(self.imapURL)
        connectionWithServer.login(self.user, self.password)
        self.connetion = connectionWithServer
        return connectionWithServer
    
    