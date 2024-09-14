def getsum(myList):
    total_sum = 0
    for row in myList:
        for item in row:
            total_sum += item
    return total_sum

print(getsum([[1, 2], [2, 2]]))
