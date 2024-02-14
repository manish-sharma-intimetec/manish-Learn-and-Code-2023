class InputValidity:
    def __init__(self, userInput):
        self.input = userInput

    def checkValidityBasedOnLength(self):
        validInput = None
        if len(self.input) != 4:
            validInput = False
        else:
            validInput = True
        return validInput

    def checkValidityBasedOnDigits(self):
        validInput = None
        charactersInInput = set()
        for i in range(len(self.input)):
            charactersInInput.add(self.input[i])
        
        if len(charactersInInput) == 1:
            validInput = False
        else:
            validInput = True
        return validInput

    def checkInputIsValidOrNot(self):
        validInput = None
        if self.checkValidityBasedOnDigits() and self.checkValidityBasedOnLength():
            validInput = True
        else:
            validInput = False
        return validInput
    