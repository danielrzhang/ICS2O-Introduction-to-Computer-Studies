userInput7 = int(input("Enter a number here: "))
userInput7a = int(input("Enter another number here: "))
userInput7b = int(input("Enter your final number here: "))

if (userInput7 < userInput7a) and (userInput7 < userInput7b):
    print(str(userInput7) + " is the smallest number!")
elif (userInput7a < userInput7) and (userInput7a < userInput7b):
    print(str(userInput7a) + " is the smallest number!")
else:
    print(str(userInput7b) + " is the smallest number!")