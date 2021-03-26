emptyList3 = []
for ages in range(50):
    ages = randint(1, 100)
    emptyList3.append(ages)
    for newNumbers in emptyList3:
        oldestAge = max(emptyList3)
        youngestAge = min(emptyList3)
        ageDifference = oldestAge - youngestAge
print(ageDifference)