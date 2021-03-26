from random import randint
emptyList = []
for i in range(10):
    i = randint(1, 1000)
    emptyList.append(i)
    sortedList = sorted(emptyList)
    reverseList = reversed(sortedList)
print(list(reverseList))