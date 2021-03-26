from random import randint
emptyList = []
newList = []
for i in range(10):
    i = randint(1, 100)
    emptyList.append(i)
print(emptyList)    

for i in emptyList:
    if i % 2 == 0:
        newList.append(i)
print(newList)