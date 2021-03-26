weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
sandwiches = ["Chicken Breast", "Steak @ Cheese", "Roast Beef", "Turkey Breast", "Spicy Italian"]
day = input("What day of the week is it? ")

index = None
for i in range(7):
    if day == weekdays[i]:
        index = i
if index == None:
    print("You have entered invalid weekday name.")
elif index < 5:
    print(weekdays[index]+"'s sandwich is",sandwiches[index] + ".")
else:
    print(weekdays[index]+" is not a promotion day.")