userInput2 = int(input("Enter a mark here: "))
if (userInput2 >= 80) and (userInput2 <= 100):
    print("You got an A!")
elif(userInput2 < 80):
    print("Try again! You can do much better!")
else:
    print("That's not a possible mark!")