#State of the program right berfore the function call: list1 and list2 are lists that can contain any type of elements.
def func_1(list1, list2):
    common_elements = set(list1) & set(list2)
    return tuple(sorted(common_elements))
    #The program returns a sorted tuple of the common elements that are found in both lists, list1 and list2, as determined by the intersection stored in the set common_elements.
#Overall this is what the function does:The function accepts two lists, `list1` and `list2`, and computes the intersection of these lists to identify common elements. It then returns a sorted tuple containing these common elements. If there are no common elements, the function will return an empty tuple. The input lists can contain any type of elements, including duplicates, but the output will only include unique common elements, sorted in ascending order.

