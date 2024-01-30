from KaprekarConstant import *


if __name__ == "__main__":
    inputNumber = takeInputFromUser()
    kaprekarConstantObj = KaprekarConstant(inputNumber)
    
    print(kaprekarConstantObj.kaprekarRoutine())