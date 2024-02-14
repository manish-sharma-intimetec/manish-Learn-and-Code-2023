from Credentials import *

class MailBox:
    def __init__(self, connection):
        self.connection = connection

    def getEmailCountForFolder(self, folderName):
        
        # self.connection.login(user, password)
        self.connection.select(mailbox = folderName)
        result, data = self.connection.search(None, "ALL")
        return len(data[0].split())