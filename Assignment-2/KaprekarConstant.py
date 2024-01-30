def takeInputFromUser():
    number = input("Enter a Number : ")

    if len(number) != 4:
        print("Invalid Input")
        return -1
    
    return int(number)

class KaprekarConstant:
    def __init__(self, number : int):
        self.number = number
        self.kaprekarConstant = 6174

    def kaprekarRoutine(self):
        number = self.number
        
        while number != self.kaprekarConstant:
            numberSortedInAccendingOrder = "".join(sorted(str(number)))
            numberSortedInDecendingOrder = "".join(sorted(str(number), reverse = True))
            number = abs(int(numberSortedInAccendingOrder) - int(numberSortedInDecendingOrder))
        
        self.number = number
        return self.number

