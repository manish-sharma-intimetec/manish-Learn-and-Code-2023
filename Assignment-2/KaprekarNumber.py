def takeValidInputFromUser():
    number = input("Enter a Number : ")

    if len(number) != 4:
        print("Invalid Input")
        return -1
    
    return int(number)

class KaprekarNumber:
    def __init__(self, number : int):
        self.number = number
        self.kaprekarConstant = 6174
        self.kaprekarIterationsOutput = []

    def kaprekarRoutine(self):
        number = self.number
        
        while number != self.kaprekarConstant:
            numberSortedInAscendingOrder = "".join(sorted(str(number)))
            numberSortedInDescendingOrder = "".join(sorted(str(number), reverse = True))
            number = abs(int(numberSortedInAscendingOrder) - int(numberSortedInDescendingOrder))
            self.kaprekarIterationsOutput.append(number)
        
        self.number = number
        return self.number
    
    def printKaprekarIterationsOutput(self):
        print("Kaprekar Iterations : ", end = "")
        for number in self.kaprekarIterationsOutput:
            print(number, end = " ")

