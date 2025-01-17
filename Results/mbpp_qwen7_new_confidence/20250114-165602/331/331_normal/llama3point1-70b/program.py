def Diff(list1, list2):
    return [element for element in list1 + list2 if (element in list1) ^ (element in list2)]
