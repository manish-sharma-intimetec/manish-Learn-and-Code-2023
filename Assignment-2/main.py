from KaprekarNumber import *
from Input import *
from InputValidity import *

if __name__ == "__main__":
    input = Input()
    userInput = input.getUserInput()

    validInputOrNot = InputValidity(str(userInput))
    
    if validInputOrNot.checkInputIsValidOrNot():
        kaprekarConstantObj = KaprekarNumber(userInput)
        print("Kaprekar value : ", kaprekarConstantObj.kaprekarRoutine())
        kaprekarConstantObj.printKaprekarIterationsOutput()
    else:
        print("Input is not Valid")