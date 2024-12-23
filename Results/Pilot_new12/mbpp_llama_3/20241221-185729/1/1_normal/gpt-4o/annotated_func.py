#State of the program right berfore the function call: list1 and list2 are lists.
def func_1(list1, list2):
    common_elements = set(list1) & set(list2)
    return tuple(sorted(common_elements))
    #The program returns a tuple containing the elements common to both list1 and list2, sorted in ascending order.
#Overall this is what the function does:The function accepts two lists, `list1` and `list2`, as parameters and returns a tuple containing the unique elements common to both lists, sorted in ascending order. The function handles duplicate elements by ignoring them, as it converts the input lists to sets before finding the common elements. If the input lists are empty or have no common elements, the function returns an empty tuple. The function does not modify the original input lists and only returns the common elements, without preserving their original order or frequency in the input lists.

