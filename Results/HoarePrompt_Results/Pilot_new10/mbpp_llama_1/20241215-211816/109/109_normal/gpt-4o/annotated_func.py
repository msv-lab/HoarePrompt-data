#State of the program right berfore the function call: list1 and list2 are lists, and list1 is not empty.
def func_1(list1, list2):
    return list1[:-1] + list2
    #The program returns a list that is the concatenation of all elements in `list1` except the last one and all elements in `list2`
#Overall this is what the function does:The function accepts two lists, `list1` and `list2`, and returns a new list that concatenates all elements in `list1` except the last one with all elements in `list2`. If `list1` is empty, it returns a copy of `list2`. If `list2` is empty, it returns all elements of `list1` except the last one.

