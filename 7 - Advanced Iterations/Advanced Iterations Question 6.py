userInputWord = str(input("Please enter a word here: "))
newWord = "";

for i in userInputWord:
    print(i)
    if (i == "a"):
        print("HI")
        newWord += "@"
        
    else:
        newWord += i
print(newWord)