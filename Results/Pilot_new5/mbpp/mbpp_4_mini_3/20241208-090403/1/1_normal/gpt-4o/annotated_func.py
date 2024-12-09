#State of the program right berfore the function call: list1 and list2 are lists that may contain any type of elements.
def func_1(list1, list2):
    common_elements = set(list1) & set(list2)
    return tuple(sorted(common_elements))
    #The program returns a sorted tuple of the common elements that are present in both 'list1' and 'list2'
#Overall this is what the function does:The function accepts two lists, `list1` and `list2`, and returns a sorted tuple of the unique common elements present in both lists. If there are no common elements, it returns an empty tuple.

