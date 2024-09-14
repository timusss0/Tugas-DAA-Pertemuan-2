def getBagi(myList):
    if not myList:
        raise ValueError("List tidak boleh kosong")
    result = myList[0]
    for item in myList[1:]:
        result /= item
    return result

print(getBagi([4,2]))