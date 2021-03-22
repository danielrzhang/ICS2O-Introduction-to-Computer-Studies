userSubject = input("Enter a subject at school: ")
userMark = input("Enter the mark you got on that subject: ")
userTotalMarks = input("Enter the total marks for that subject: ")

userPercentage = int(userMark) / int(userTotalMarks)
userRound = round(userPercentage, 3)

print("Your percentage mark in " + userSubject + " was " + str(userRound * 100) +  "%.")

