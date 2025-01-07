#State of the program right berfore the function call: list1 and list2 are lists that can contain any type of elements.
def func_1(list1, list2):
    common_elements = set(list1) & set(list2)
    return tuple(sorted(common_elements))
    #The program returns a sorted tuple of the common elements between list1 and list2, which are stored in the set common_elements.
#Overall this is what the function does:The function accepts two lists, list1 and list2, and returns a sorted tuple of the common elements between the two lists. If there are no common elements, it returns an empty tuple.

