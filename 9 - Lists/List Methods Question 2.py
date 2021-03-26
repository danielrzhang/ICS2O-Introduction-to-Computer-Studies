numInput1 = int(input("Enter a number here: "))
numInput2 = int(input("Enter another number here: "))
numInput3 = int(input("Enter another number here: "))
numInput4 = int(input("Enter another number here: "))
numInput5 = int(input("Enter another number here: "))
emptyList = []
emptyList.append(numInput1)
emptyList.append(numInput2)
emptyList.append(numInput3)
emptyList.append(numInput4)
emptyList.append(numInput5)
if emptyList[0] <= emptyList[1] <= emptyList[2] <= emptyList[3] <= emptyList[4]:
    print("The list is sorted.")
else:
    print("The list is not sorted.")