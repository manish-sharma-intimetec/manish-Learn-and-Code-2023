#include "Email.h"
#include "IEntity.h"
#include <iostream>

int main()
{
    int spamEmails, standardEmail, emailWithAttachments;
    std::cout << "Enter the number of spam mails: ";
    std::cin >> spamEmails;
    std::cout << "Enter the number of standard mails: ";
    std::cin >> standardEmail;
    std::cout << "Enter the number of emails with attachments: ";
    std::cin >> emailWithAttachments;
    IEntity* entity = new Email(spamEmails, standardEmail, emailWithAttachments);
    double footPrint = entity->calculateFootPrint();
    std::cout << "\nYou have " << footPrint << " amount of carbon foot print\n";
    return 0;
}
