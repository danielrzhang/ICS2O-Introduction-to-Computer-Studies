userInputVowelWord = str(input("Please enter a word here: "))
newCharacter = "@"

for i in userInputVowelWord:
    if (i == "a") or (i == "e") or (i == "i") or (i == "o") or (i == "u"):
        userInputVowelWord += newCharacter
print(userInputVowelWord)