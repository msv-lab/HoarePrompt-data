#State of the program right berfore the function call: list1 and list2 are both lists.
def func_1(list1, list2):
    return list1[:-1] + list2
    #The program returns a new list that contains all elements of list1 except the last element, followed by all elements of list2
#Overall this is what the function does:The function `func_1` accepts two lists, `list1` and `list2`, and returns a new list that contains all elements of `list1` except the last element, followed by all elements of `list2`. This holds true for all possible inputs, including edge cases where either or both lists are empty.

