def func_1(arr, x):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == x:
            return i
    return -1
assert func_1([1, 2, 3], 1) == 0
assert func_1([1, 1, 1, 2, 3, 4], 1) == 2
assert func_1([2, 2, 3, 3, 6, 8, 9], 3) == 3