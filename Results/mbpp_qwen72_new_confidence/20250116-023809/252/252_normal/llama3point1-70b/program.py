def swap_List(inputList):
    if len(inputList) > 1:
        inputList[0], inputList[-1] = inputList[-1], inputList[0]
    return inputList
