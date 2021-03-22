from random import randint
randNumber = randint(1, 10)

userInput4 = int(input("Enter a number between 1 to 10 here: "))
if randNumber == userInput4:
    print("You guessed the correct number!")
else:
    print("Not quite. Try again!")