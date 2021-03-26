inputQ1width = float(input("Enter the width of the sandbox in centimeters: "))
inputQ1length = float(input("Enter the length of the sandbox in centimeters: "))
inputQ1height = float(input("Enter the height of the sandbox in centimeters: "))


volumeQ1 = inputQ1width * inputQ1length * inputQ1height
weightQ1 = int(volumeQ1) * 3

print("The volume of the sandbox is " + str(volumeQ1) + " cubic centimeters and the weight of the sandbox is " + str(weightQ1) + " grams.")