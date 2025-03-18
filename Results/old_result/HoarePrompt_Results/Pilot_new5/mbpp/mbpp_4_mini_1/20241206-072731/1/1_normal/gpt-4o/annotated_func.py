#State of the program right berfore the function call: list1 and list2 are lists that may contain any data types.
def func_1(list1, list2):
    common_elements = set(list1) & set(list2)
    return tuple(sorted(common_elements))
    #The program returns a tuple of the sorted common elements that are in both `list1` and `list2`, with `common_elements` being a set of those elements.
#Overall this is what the function does:The function accepts two lists, `list1` and `list2`, and returns a tuple containing the sorted common elements found in both lists. It does not handle the case where either list is empty; in such a scenario, the function will return an empty tuple since there would be no common elements to sort. Additionally, the function correctly accounts for elements of any data type present in the lists.

