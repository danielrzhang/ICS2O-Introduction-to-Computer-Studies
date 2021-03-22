userInput5 = int(input("Enter the number of tickets you would like to buy: "))
under4Cost = 12.50
above4Cost = 8.95
totalCostBelow4 = userInput5 * under4Cost
totalCostAbove4 = userInput5 * above4Cost


if userInput5 < 4:
    print("The cost of", userInput5, "tickets costs", round(totalCostBelow4, 4), "dollars.")
else:
    print("The cost of", userInput5, "tickets costs", round(totalCostAbove4, 4), "dollars.")