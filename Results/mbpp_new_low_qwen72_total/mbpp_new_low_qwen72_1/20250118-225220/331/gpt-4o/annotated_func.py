#State of the program right berfore the function call: list1 and list2 are lists.
def func_1(list1, list2):
    set1 = set(list1)

set2 = set(list2)

diff_elements = set1.symmetric_difference(set2)

result_list = list(diff_elements)

result_list.sort(key=lambda x: (list1 + list2).index(x))
    return result_list
    #The program returns a sorted list of elements in `diff_elements` based on their first occurrence in the concatenated list of `list1` and `list2`. `diff_elements` is a set containing elements that are in either `list1` or `list2` but not in both.
#Overall this is what the function does:The function `func_1` accepts two parameters, `list1` and `list2`, both of which are lists. It returns a sorted list of elements that are present in either `list1` or `list2` but not in both, based on their first occurrence in the concatenated list of `list1` and `list2`. If either `list1` or `list2` is empty, the function will return the non-empty list sorted by the order of their first occurrence in the non-empty list. If both lists are empty, the function will return an empty list.

