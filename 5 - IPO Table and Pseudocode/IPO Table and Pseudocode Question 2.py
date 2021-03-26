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