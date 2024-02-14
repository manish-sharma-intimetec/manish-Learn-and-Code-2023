class Input:
    def __init__(self):
        self.userInput = None
    
    def getUserInput(self):
        self.userInput = int(input("Enter the Number : "))
        return self.userInput