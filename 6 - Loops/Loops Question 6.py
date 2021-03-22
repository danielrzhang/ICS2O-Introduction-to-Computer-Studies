from random import randint
number = randint(0,1)

userInputAnswer = str(input("Guess heads or tails: "))

while ((number != 0) and (userInputAnswer == "Heads") or (userInputAnswer == "heads")) or ((number != 1) and (userInputAnswer == "Tails") or userInputAnswer == "tails"):
    print("Nice guess, but try again!")
    number = randint(0,1)
    userInputAnswer = str(input("\nGuess heads or tails again: "))