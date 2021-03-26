inputQ3Name = str(input("What is your full name? "))
inputQ3Cake = float(input("How many slices of cake have you eaten? "))

cakeCalories = 225 * inputQ3Cake
userJoggingDistance = float(cakeCalories) / 100
roundedJoggingDistance = round(userJoggingDistance, 2)

print(str(inputQ3Name) + ", you must jog " + str(userJoggingDistance) + " km to burn off " + str(inputQ3Cake) + " slices of cake worth of calories.")