userInput9 = str(input("How are you feeling? "))

if (userInput9 == "Tired") or (userInput9 == "Sleepy"):
    print("You should probably go to bed early.")
if (userInput9 == "Sad"):
    print("Try smiling!")
if (userInput9 == "Happy"):
    print("Do you want to go to a party?")
else:
    print("Not a valid answer. Try again!")