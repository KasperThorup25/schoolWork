# Lavet af Kasper Thorup

# Function for calculating the name score, which returns the average ascii value of the letters in the given name
def calculateNameScore(name):
    totalScore = 0
    for i in range(len(name)):
        totalScore += ord(name[i])  # The function "ord" is used to get the ascii values
    return round(totalScore / len(name))


while (True):
    userName = input("What's your name? ")

    if "mark" in userName.lower():
        print("This name is unable to be processed due to bad name")
        exit("ID10T")


    # The name is converted to only lowercase to prevent different outcomes
    userNameScore = calculateNameScore(userName.lower())

    if userNameScore < 105:
        print("Your name sucks...")
    elif userNameScore < 106:
        print("Your name is bad")
    elif userNameScore < 107:
        print("Your name is okay")
    else:
        print("Your name is awesome!!")

    print("Your name score is: ", userNameScore)

    continueUserInput = input("Do you wanna try again (n/y)? ")
    if continueUserInput.lower() == "n":
        break




