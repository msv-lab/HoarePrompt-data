#State of the program right berfore the function call: list1 and list2 are lists.
def func_1(list1, list2):
    set1 = set(list1)

set2 = set(list2)

diff_elements = set1.symmetric_difference(set2)

result_list = list(diff_elements)

result_list.sort(key=lambda x: (list1 + list2).index(x))
    return result_list
    #The program returns a sorted list of elements from `diff_elements` based on their first occurrence in the concatenated list (`list1 + list2`). `diff_elements` contains the elements that are in either `list1` or `list2` but not in both.
#Overall this is what the function does:The function `func_1` takes two lists, `list1` and `list2`, and returns a sorted list of elements that are present in either `list1` or `list2` but not in both. The sorting is based on the order of their first occurrence in the concatenated list (`list1 + list2`). If either `list1` or `list2` is empty, the function will return a sorted list of the non-empty list's elements. If both lists are empty, the function will return an empty list. The function ensures that the resulting list contains unique elements that are not shared between the two input lists.

