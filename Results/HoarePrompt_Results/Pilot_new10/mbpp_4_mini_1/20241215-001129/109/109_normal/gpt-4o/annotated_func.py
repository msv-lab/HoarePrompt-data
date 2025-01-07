#State of the program right berfore the function call: list1 and list2 are both lists. list1 has at least one element.
def func_1(list1, list2):
    return list1[:-1] + list2
    #The program returns all elements of list1 except the last one, concatenated with all elements of list2.
#Overall this is what the function does:The function accepts two lists, `list1` and `list2`, and returns a new list that consists of all elements from `list1` except the last one, concatenated with all elements from `list2`. If `list1` contains only one element, the result will be the contents of `list2` alone.

