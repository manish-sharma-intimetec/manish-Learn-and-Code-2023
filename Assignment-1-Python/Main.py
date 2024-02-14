from EmailConnection import *
from MailBox import *
from CarbonFootPrint import *

emailConnection = EmailConnection()
userMailBox = MailBox(emailConnection.makeConnectionWithGmailServer())

inboxEmailsCount = userMailBox.getEmailCountForFolder("Inbox")
spamEmailsCount = userMailBox.getEmailCountForFolder("[Gmail]/Spam")
draftEmailsCount = userMailBox.getEmailCountForFolder("[Gmail]/Drafts")


carbonFootPrint = CarbonFootPrint()
totalCarbonFootPrint = carbonFootPrint.calculateCarbonFootPrint(inboxEmailsCount, spamEmailsCount, draftEmailsCount)

print(totalCarbonFootPrint, "g")