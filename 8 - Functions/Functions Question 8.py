def hypotenuse(leg1, leg2):
        result = ((leg1 ** 2) + (leg2 ** 2)) ** 0.5
        return result
    
def getLineLength(num1X, num1Y, num2X, num2Y): 
        lineXResult = point2X - point1X
        lineYResult = point2Y - point1Y
        lineResult = lineYResult / pointXResult
        return lineResult
    
def getLineSlope(point1X, point1Y, point2X, point2Y):
        lineXResult = point2X - point1X
        lineYResult = point2Y - point1Y
        lineResult = lineYResult / pointXResult
        return lineResult
    
    
userSelect = str(input("Please choose an option - Hypotenuse, Length, or Slope: "))

if userSelect == "Hypotenuse":
    legSide1 = int(input("Please enter the length of the side of a triangle leg here: "))
    legSide2 = int(input("Now, please enter the length of the side of another triangle leg here: "))
    variableHypotenuse = hypotenuse(legSide1, legSide2)
    print(variableHypotenuse)
    
elif (userSelect == "Length") or (userSelect == "Slope"):
    pointNumber1X = int(input("Please enter the x-coordinate of the first point here: "))
    pointNumber1Y = int(input("Please enter the y-coordinate of the first point here: "))
    pointNumber2X = int(input("Please enter the x-coordinate of the second point here: "))
    pointNumber2Y = int(input("Please enter the y-coordinate of the second point here: "))  
    
    if (userSelect == "Length"):
        variableGetLineLength = getLinelength(pointNumber1X, pointNumber1Y, pointNumber2X, pointNumber2Y)
        print(variableGetLineLength)
        
    else: 
        variableGetLineSlope = getLineSlope(pointNumber1X, pointNumber1Y, pointNumber2X, pointNumber2Y)
        print(variableGetLineSlope)
    
else:
    print("That is not a valid selection! Try again!")
    
    




