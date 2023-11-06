#include "Email.h"

Email::Email(int spamEmailCount, int standardEmailCount, int emailWithAttachmentsCounts)
 : spamEmailCount{spamEmailCount}, standardEmailCount{standardEmailCount}, emailWithAttachmentsCounts{emailWithAttachmentsCounts}
{
}

double Email::calculateCarbonFootPrint()
{
    double footPrint;
    footPrint = spamEmailCount * spamEmail + standardEmailCount * standardEmail + emailWithAttachmentsCounts * emailWithAttachments;
    return footPrint;
}