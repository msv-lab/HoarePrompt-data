#State of the program right berfore the function call: list1 and list2 are both lists, which may contain elements of any data type.
def func_1(list1, list2):
    common_elements = set(list1) & set(list2)
    return tuple(sorted(common_elements))
    #The program returns a tuple containing the elements present in both 'list1' and 'list2', sorted in ascending order.
#Overall this is what the function does:The function accepts two lists, `list1` and `list2`, and returns a tuple containing the common elements found in both lists, sorted in ascending order. If there are no common elements, an empty tuple is returned. The function handles elements of any data type present in the lists.

