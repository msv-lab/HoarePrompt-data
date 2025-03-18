def func_1(list1, list2):
    return list1[:-1] + list2
assert func_1([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 2, 4, 6, 8]
assert func_1([1, 2, 3, 4, 5], [5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
assert func_1(['red', 'blue', 'green'], ['yellow']) == ['red', 'blue', 'yellow']