#State of the program right berfore the function call: list1 and list2 are lists.
def func_1(list1, list2):
    set1 = set(list1)

set2 = set(list2)

diff_elements = set1.symmetric_difference(set2)

result_list = list(diff_elements)

result_list.sort(key=lambda x: (list1 + list2).index(x))
    return result_list
    #The program returns a sorted list of elements that are in either list1 or list2 but not in both, based on their first occurrence in the concatenated list list1 + list2
#Overall this is what the function does:The function `func_1` accepts two parameters, `list1` and `list2`, both of which are lists. It returns a sorted list of elements that are present in either `list1` or `list2` but not in both. The sorting is based on the first occurrence of each element in the concatenated list `list1 + list2`. If either `list1` or `list2` is empty, the function will return a sorted list of elements from the non-empty list. If both lists are empty, the function will return an empty list.

