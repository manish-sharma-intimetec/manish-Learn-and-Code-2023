#include "Email.h"
#include "IEntity.h"
#include <iostream>

int main()
{
    int spamEmailsCount, standardEmailCount, emailWithAttachmentsCount;
    std::cout << "Enter the number of spam mails: ";
    std::cin >> spamEmailsCount;
    std::cout << "Enter the number of standard mails: ";
    std::cin >> standardEmailCount;
    std::cout << "Enter the number of emails with attachments: ";
    std::cin >> emailWithAttachmentsCount;
    IEntity* entity = new Email(spamEmailsCount, standardEmailCount, emailWithAttachmentsCount);
    double footPrint = entity->calculateCarbonFootPrint();
    std::cout << "\nYou have " << footPrint << " amount of carbon foot print\n";
    return 0;
}
