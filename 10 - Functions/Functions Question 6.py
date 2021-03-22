from random import randint

number = randint(65, 90)
def getRandomLetter(num):
    return chr(num)

variableGetRandomLetter = getRandomLetter(number)
print(variableGetRandomLetter)