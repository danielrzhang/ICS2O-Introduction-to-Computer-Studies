longWord = "Pneumonoultramicroscopicsilicovolcanoconiosis"
userInputLetter = str(input("Enter any letter: "))
letterCount = 0

for i in longWord:
    if i == userInputLetter:
        letterCount += 1
print("The letter " + userInputLetter + " is used " + str(letterCount) + " times in the word '" + longWord + ".'")