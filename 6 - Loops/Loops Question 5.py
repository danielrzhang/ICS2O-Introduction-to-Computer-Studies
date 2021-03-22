userInputSubject = str(input("Enter a subject here: "))
userInputMark = input("Enter the mark you got in that subject: ")

while (userInputSubject != "") and (userInputMark >= 0) or (userInputMark != ""):
    print("You got a mark of " + str(userInputMark) + " in " + str(userInputSubject) + ".")
    userInputSubject = str(input("Enter another subject here: "))
    userInputMark = float(input("Enter another mark here: "))