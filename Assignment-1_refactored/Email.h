#ifndef EMAIL_H
#define EMAIL_H

#include "IEntity.h"

class Email : public IEntity
{
public:
    Email(int spamEmailCount, int standardEmailCount, int emailWithAttachmentsCounts);
    double calculateCarbonFootPrint() override;

private:
    const double spamEmail = 0.3;
    const double standardEmail = 4.0;
    const double emailWithAttachments = 50.0;
    int spamEmailCount, standardEmailCount, emailWithAttachmentsCounts;
};

#endif