def func_1(list1, list2):
    common_elements = set(list1) & set(list2)
    return tuple(sorted(common_elements))
assert func_1((3, 4, 5, 6), (5, 7, 4, 10)) == (4, 5)
assert func_1((1, 2, 3, 4), (5, 4, 3, 7)) == (3, 4)
assert func_1((11, 12, 14, 13), (17, 15, 14, 13)) == (13, 14)