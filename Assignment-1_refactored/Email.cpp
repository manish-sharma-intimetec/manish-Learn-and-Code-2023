#include "Email.h"

Email::Email(int m_spamEmailCount, int m_standardEmailCount, int m_emailWithAttachmentsCounts)
 : spamEmailCount{m_spamEmailCount}, standardEmailCount{m_standardEmailCount}, emailWithAttachmentsCounts{m_emailWithAttachmentsCounts}
{
}

double Email::calculateFootPrint()
{
    double footPrint;
    footPrint = spamEmailCount * spamEmail + standardEmailCount * standardEmail + emailWithAttachmentsCounts * emailWithAttachments;
    return footPrint;
}