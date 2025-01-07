def func_1(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    diff_elements = set1.symmetric_difference(set2)
    result_list = list(diff_elements)
    result_list.sort(key=lambda x: (list1 + list2).index(x))
    return result_list
assert func_1([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]) == [10, 20, 30, 15]
assert func_1([1, 2, 3, 4, 5], [6, 7, 1]) == [2, 3, 4, 5, 6, 7]
assert func_1([1, 2, 3], [6, 7, 1]) == [2, 3, 6, 7]