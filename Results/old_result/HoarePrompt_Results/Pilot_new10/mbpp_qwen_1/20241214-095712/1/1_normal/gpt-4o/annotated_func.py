#State of the program right berfore the function call: list1 and list2 are lists.
def func_1(list1, list2):
    common_elements = set(list1) & set(list2)
    return tuple(sorted(common_elements))
    #The program returns a tuple containing the sorted elements from the set common_elements, which contains elements present in both list1 and list2
#Overall this is what the function does:The function `func_1` accepts two lists, `list1` and `list2`, finds the common elements between them, converts those elements into a set, sorts them, and returns them as a tuple. The function handles the case where either or both lists are empty by returning an empty tuple.

