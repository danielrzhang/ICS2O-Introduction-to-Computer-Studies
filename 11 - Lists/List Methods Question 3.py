wordInput1 = str(input("Enter a word here: "))
wordInput2 = str(input("Enter another word here: "))
list1 = list(wordInput1)
list2 = list(wordInput2)
for letters in list1:
    lengthList1 = len(list1)
for letters in list2:
    lengthList2 = len(list2)
if lengthList1 > lengthList2:
    print("The first word is longer than the second word")
else:
    print("The second word is equal to or longer than the first word.")