def func_1(list1, list2, n):
    merged_list = sorted(list1 + list2)
    mid = len(merged_list) // 2
    if len(merged_list) % 2 == 0:
        median = (merged_list[mid - 1] + merged_list[mid]) / 2
    else:
        median = merged_list[mid]
    return median
assert func_1([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
assert func_1([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
assert func_1([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0