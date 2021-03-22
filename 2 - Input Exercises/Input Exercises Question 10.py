userInput = input("Enter the principal amount of money: ")
userInput1 = input("Enter the interest rate in percent: ")
userInput2 = input("Enter the amount of time invested: ")

amountInterest = int(userInput) * (int(userInput1) / 100) * int(userInput2)
roundedInterest = round(float(amountInterest), 3)

print("The amount of simple interest earned is $" + str(roundedInterest) + ".")
