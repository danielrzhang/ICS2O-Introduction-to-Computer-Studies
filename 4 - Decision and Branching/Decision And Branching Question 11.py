userInput11Rate = int(input("Enter your hourly rate of pay here: "))
userInput11Time = int(input("Enter the number of hours you worked this week: "))
userInput11Tax = str(input("Enter your tax category letter: "))
userHourlyPay = userInput11Time * userInput11Rate

if int(userInput11Time) <= 40:
    grossPay = userHourlyPay
else:
    grossPay = ((userInput11Rate * 2) * (userInput11Time - 40)) + (userInput11Rate * 40)
          
if userInput11Tax == "A":
    tax = grossPay * 0
elif userInput11Tax == "B":
    tax = grossPay * 0.1
elif userInput11Tax == "C":
    tax = grossPay * 0.2
elif userInput11Tax == "D":
    tax = grossPay * 0.29
elif userInput11Tax == "E":
    tax = grossPay * 0.35
else:
    print("Not a valid tax deduction!")
netPay = int(grossPay) - int(tax)
    
print("The gross pay is $" + str(grossPay) + ", the tax deduction is $" + str(tax) + ", and the net pay is $" + str(netPay) + ".") 
