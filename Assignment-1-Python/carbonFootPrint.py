import imaplib
import email


standardEmails = 0
spamEmails = 0


user = "manish.sharma.intimetec@gmail.com"
password = "uhst ymou sids ifdt"
imapURL = "imap.gmail.com"


def makeConnectionWithGmailServer():
    connectionWithServer = imaplib.IMAP4_SSL(imapURL)
    connectionWithServer.login(user, password)
    return connectionWithServer


def getEmailCountForFolder(serverConnection, folderName):
    serverConnection.select(folderName)
    result, data = serverConnection.search(None, "ALL")
    return len(data[0].split())

#connection with gmail server......
# connectionWithServer = imaplib.IMAP4_SSL(imapURL)

# connectionWithServer.login(user, password)

# connectionWithServer.select("Inbox")

# result, data = connectionWithServer.search(None, "ALL")



connectionWithServer = makeConnectionWithGmailServer()
standardEmails = getEmailCountForFolder(connectionWithServer, "")


connectionWithServer = makeConnectionWithGmailServer()
spamEmails = getEmailCountForFolder(connectionWithServer, "Inbox")

# connectionWithServer.select("Spam")
# result, data = connectionWithServer.search(None, "ALL")
# spamEmails = len(data[0].split())

print(spamEmails)
print(standardEmails)