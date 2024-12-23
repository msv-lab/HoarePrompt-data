#State of the program right berfore the function call: list1 and list2 are lists containing elements, and the elements can be of any data type.
def func_1(list1, list2):
    common_elements = set(list1) & set(list2)
    return tuple(sorted(common_elements))
    #The program returns a tuple containing the sorted elements that are present in both lists 'list1' and 'list2', represented by the set 'common_elements'.
#Overall this is what the function does:The function accepts two parameters, `list1` and `list2`, which are lists containing elements of any data type. It computes the intersection of these two lists, identifying the elements that are present in both. It then sorts these common elements, converts them into a tuple, and returns this tuple. If there are no common elements, the function returns an empty tuple. The function effectively filters out duplicates since it utilizes sets for the intersection, ensuring all returned items are unique.

