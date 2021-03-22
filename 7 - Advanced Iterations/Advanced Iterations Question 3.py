userInputCharacter = str(input("Please enter a letter to make a word: "))
newWord = ""

while userInputCharacter != "":
    newWord += str(userInputCharacter)
    userInputCharacter = str(input("Please enter another letter to make a word: "))
print(newWord)