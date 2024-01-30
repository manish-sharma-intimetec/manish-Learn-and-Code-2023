#ifndef IENTITY_H
#define IENTITY_H

#include <string>

class IEntity
{
public:
    virtual double calculateCarbonFootPrint() = 0;
};

#endif