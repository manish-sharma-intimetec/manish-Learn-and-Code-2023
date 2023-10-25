#include<iostream>
using namespace std;

class email
{
private:
    double averageFootPrintForSpam = 0.3, averageFootPrintForStdMail = 4, averageFootPrintForAttachementMail;
    int spamCount, stdEmailCount, emailsWithAttachments = 50;

public:
    email()
    {

    }

    email(int spamCount, int stdEmailCount, int emailsWithAttachments)
    {
        this->stdEmailCount = stdEmailCount;
        this->spamCount = this->spamCount;
        this->emailsWithAttachments = emailsWithAttachments;
    }

    void setCountForEmailInbox(int spamCount, int stdEmailCount, int emailsWithAttachments)
    {   
        this->stdEmailCount = stdEmailCount;
        this->spamCount = this->spamCount;
        this->emailsWithAttachments = emailsWithAttachments;
    }

    double getEmailFootPrint()
    {
        double footPrintValue = 0;

        footPrintValue += (this->spamCount * this->averageFootPrintForSpam) + (this->stdEmailCount * this->averageFootPrintForStdMail) + (this->emailsWithAttachments + this->averageFootPrintForAttachementMail);
    }
};


int askUserEntityType()
{   
    int entityType = -1;
    cout << "Enter 1 for Emails, Enter 2 for Server and 3 for Something : ";
    cout << "Enter Entity Type : ";

    cin >> entityType;
    return entityType;
}

int main()
{
    int result = -1;
    int entityType = askUserEntityType();

    if (entityType == 1)
    {
        email emailObject(1, 3 , 4);
        result = emailObject.getEmailFootPrint();
    }
    
}