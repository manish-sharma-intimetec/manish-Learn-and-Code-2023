class CarbonFootPrint:
    def calculateCarbonFootPrint(self, spamEmails, inboxEmails, draftEmails):
        totalCarbonFootPrint = 0.03 * spamEmails + 0.2 * inboxEmails + 	17 * draftEmails
        return totalCarbonFootPrint