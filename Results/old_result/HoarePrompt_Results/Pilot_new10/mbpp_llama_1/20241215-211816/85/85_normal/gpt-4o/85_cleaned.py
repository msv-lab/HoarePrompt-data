def func_1(arr):
    min_val = min(arr)
    max_val = max(arr)
    max_diff = max_val - min_val
    return max_diff
assert func_1((2, 1, 5, 3)) == 4
assert func_1((9, 3, 2, 5, 1)) == 8
assert func_1((3, 2, 1)) == 2