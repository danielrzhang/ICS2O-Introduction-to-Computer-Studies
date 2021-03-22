##########################################
# File Name: HangmanProject.py           #
# Description: Formative Hangman Project #
# Author: Daniel Zhang                   #
# Date: 09/24/2019                       #
##########################################

secretWord = "CODING"
dashes = "-"
MISTAKE_LIMIT = 7
mistakes = 0
usedLetters = ""
guess = str(input("Enter a letter here: "))

while (mistakes <= MISTAKE_LIMIT) and (usedLetters != secretWord):
    for letter in secretWord:
        if letter in usedLetters:
            print("You already guessed that letter! Try again!")
        else:
            if guess in secretWord:
                usedLetters += guess
                print("You guessed the letter " + guess + ". It is in the secret word!")
                print("You have " + str(mistakes) + " mistakes!")
                print("You have used the letters " + usedLetters)
                guess = str(input("Enter another letter here: "))
            else:
                usedLetters += guess
                mistakes += 1
                print("You have guessed the letter " + guess + ". It is not in the secret word.")
                print("You have " + str(mistakes) + " mistakes!")
                print("You have used the letters " + usedLetters)
                guess = str(input("Enter another letter here: "))
############################################################################
dash = ""
MISTAKE_LIMIT = 7
mistakes = 0
usedLetters = ""
guessed = False

while (mistakes <= MISTAKE_LIMIT) and (not guessed):
    
    dash =""
    for letter in secretWord:
        if letter in usedLetters:
            dash = dash + letter
        else:
            dash = dash + "-"
            
    print(dash)
    print( "Used letters:",usedLetters)
    
    if not "-" in dash:
        print("You win!")
        guessed = True

    else:
        guess = input("guess a letter: ")
        if guess not in usedLetters:
            usedLetters = usedLetters + guess

        if guess not in secretWord:
            mistakes = mistakes + 1
            print ("Nope. You have", MISTAKE_LIMIT - mistakes,"mistakes left.")

print ("The answer is", secretWord)
        
        
        
    
    








































































































































































































































































































































































                    
                
                

        #if guess in secretWord:
            #print("C")
        #else:
            #print(dashes)
            
            
                
            
            
            
        
            
        
            



            

    
            


                

            
            
            
            



            



        


        
                

            
            
            
            



            

