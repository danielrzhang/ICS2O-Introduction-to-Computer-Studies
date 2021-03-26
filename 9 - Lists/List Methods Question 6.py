from random import randint
number1 = randint(1, 49)
number2 = randint(1, 49)
number3 = randint(1, 49)
number4 = randint(1, 49)
number5 = randint(1, 49)
number6 = randint(1, 49)
emptyList = []
while number6 not in emptyList:
    emptyList.append(number1)
    if number2 not in emptyList:
        emptyList.append(number2)
    else:
        number2 = randint(1, 49)
    if number3 not in emptyList:
        emptyList.append(number3)
    else:
        number3 = randint(1, 49)
    if number4 not in emptyList:
        emptyList.append(number4)
    else:
        number4 = randint(1, 49)
    if number5 not in emptyList:
        emptyList.append(number5)
    else:
        number5 = randint(1, 49)
    if number6 not in emptyList:
        emptyList.append(number6)
    else:
        number6 = randint(1, 49)
print(emptyList)