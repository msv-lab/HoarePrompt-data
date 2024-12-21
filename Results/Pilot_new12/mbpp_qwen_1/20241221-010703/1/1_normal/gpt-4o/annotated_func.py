#State of the program right berfore the function call: list1 and list2 are lists.
def func_1(list1, list2):
    common_elements = set(list1) & set(list2)
    return tuple(sorted(common_elements))
    #The program returns a tuple containing the sorted elements present in both `list1` and `list2`
#Overall this is what the function does:The function `func_1` accepts two lists, `list1` and `list2`, and returns a tuple containing the sorted common elements found in both lists. If either `list1` or `list2` is empty, the function will return an empty tuple. If there are no common elements between the two lists, it will also return an empty tuple. The function ensures that the returned tuple contains only the unique elements that are present in both input lists, sorted in ascending order.

