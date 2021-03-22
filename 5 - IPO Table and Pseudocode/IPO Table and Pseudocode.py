#Question 1: Sandbox
inputQ1width = float(input("Enter the width of the sandbox in centimeters: "))
inputQ1length = float(input("Enter the length of the sandbox in centimeters: "))
inputQ1height = float(input("Enter the height of the sandbox in centimeters: "))


volumeQ1 = inputQ1width * inputQ1length * inputQ1height
weightQ1 = int(volumeQ1) * 3

print("The volume of the sandbox is " + str(volumeQ1) + " cubic centimeters and the weight of the sandbox is " + str(weightQ1) + " grams.")

#Question 2: Body Measurements
inputQ2Kilograms = input("Enter your weight in kilograms here: ")
inputQ2Meters = input("Enter your height in meters here: ")

userBMI = float(inputQ2Kilograms) / (float(inputQ2Meters) ** 2)
userBSA = ((float(inputQ2Kilograms) * float(inputQ2Meters)) / 36) ** 0.5
roundedBMI = round(userBMI, 2)
roundedBSA = round(userBSA, 2)

print("Your Body Mass Index is " + str(roundedBMI) + " and your Body Surface Area is " + str(roundedBSA) + ".")
if (roundedBMI >= 18.5) and (roundedBMI <= 25):
    print("Your weight is relatively healthy.")
else:
    print("Your weight is not too healthy.")
    
#Question 3: Calories
inputQ3Name = str(input("What is your full name? "))
inputQ3Cake = float(input("How many slices of cake have you eaten? "))

cakeCalories = 225 * inputQ3Cake
userJoggingDistance = float(cakeCalories) / 100
roundedJoggingDistance = round(userJoggingDistance, 2)

print(str(inputQ3Name) + ", you must jog " + str(userJoggingDistance) + " km to burn off " + str(inputQ3Cake) + " slices of cake worth of calories.")



