#State of the program right berfore the function call: list1 and list2 are both lists.
def func_1(list1, list2):
    return list1[:-1] + list2
    #The program returns all elements of list1 except the last one concatenated with all elements of list2
#Overall this is what the function does:The function accepts two lists, `list1` and `list2`, and returns a new list that includes all elements of `list1` except the last one, concatenated with all elements of `list2`. If `list1` is empty, it will return an empty list concatenated with `list2` and if `list2` is also empty, it will return all elements of `list1` except the last one. If both lists are empty, it returns an empty list.

