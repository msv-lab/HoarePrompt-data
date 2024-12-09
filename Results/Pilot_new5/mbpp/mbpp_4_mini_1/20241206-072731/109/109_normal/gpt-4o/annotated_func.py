#State of the program right berfore the function call: list1 and list2 are both lists, and list1 has at least one element.
def func_1(list1, list2):
    return list1[:-1] + list2
    #The program returns a new list that combines all elements of list1 except the last element with all elements of list2.
#Overall this is what the function does:The function accepts two lists, `list1` and `list2`, and returns a new list that contains all elements of `list1` except the last element, combined with all elements of `list2`. If `list1` has only one element, the returned list will only contain the elements of `list2`.

