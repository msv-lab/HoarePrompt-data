def func_1(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(func_1(item))
        else:
            flat_list.append(item)
    return flat_list
assert func_1([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]) == [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
assert func_1([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]) == [10, 20, 40, 30, 56, 25, 10, 20, 33, 40]
assert func_1([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]) == [1, 2, 3, 4, 5, 6, 10, 11, 12, 7, 8, 9]