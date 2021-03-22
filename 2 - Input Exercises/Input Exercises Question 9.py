userInput = input("Enter the radius of a circle: ")

circleCircumference = 2 * 3.14 * int(userInput)
circumferenceRounded = round(float(circleCircumference), 3)

print("The circumference of a circle with radius " + str(userInput) + " is " + str(circumferenceRounded) + ".")
