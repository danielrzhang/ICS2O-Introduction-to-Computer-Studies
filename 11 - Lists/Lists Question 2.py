from random import randint
emptyList2 = []
for numbers in range(15):
    numbers = randint(0, 1000)
    emptyList2.append(numbers)
    for newNumbers in emptyList2:
        newNumbers = sum(emptyList2)
        result = newNumbers / 15
print(result)