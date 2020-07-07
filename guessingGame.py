import random

def generateRandomNumber():
    randomNumber = random.randInt(1,9)
    return randomNumber

def askUserForNumber(message = "Guess the number"):
    userNumber = int(input(message))
    return userNumber

def checkUserForNumber(userNumber,randomNumber):
    if userNumber>randomNumber:
        return "Too high"
    elif userNumber<randomNumber:
        return "Too low"
    else:
        return "Conratulations!"

def main():
    userCongratulated = False
    letsStart = True

    while userCongratulated or letsStart:
        randomNumber = generateRandomNumber()
        userNumber = askUserForNumber()
        message = checkUserForNumber(userNumber,randomNumber)

    while message != "Congratulations!":
        print(message)
        userNumber = askUserForNumber("Try again:")
        message = checkUserForNumber(userNumber,randomNumber)
    
    print(message)
    userCongratulated = True
