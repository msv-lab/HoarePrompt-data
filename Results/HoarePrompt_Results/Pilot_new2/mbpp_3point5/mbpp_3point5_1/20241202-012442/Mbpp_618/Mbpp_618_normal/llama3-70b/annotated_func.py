#State of the program right berfore the function call: list1 and list2 are lists of the same length containing integers.**
def func_1(list1, list2):
    if (len(list1) != len(list2)) :
        raise ValueError('Both lists must be of the same length')
    #State of the program after the if block has been executed: *list1 and list2 are lists of the same length containing integers. If the length of list1 is not equal to the length of list2, a ValueError is raised stating 'Both lists must be of the same length'.
    return [(x / y) for x, y in zip(list1, list2)]
    #The program returns a list of the same length as list1 and list2, where each element in the list is the result of dividing the corresponding elements in list1 by list2. If the length of list1 is not equal to the length of list2, a ValueError is raised stating 'Both lists must be of the same length'.
#Overall this is what the function does:The function func_1 accepts two lists, list1 and list2, containing integers of the same length. It then returns a new list where each element is the result of dividing the corresponding elements in list1 by list2. If the lengths of list1 and list2 are not equal, a ValueError is raised stating 'Both lists must be of the same length'.

