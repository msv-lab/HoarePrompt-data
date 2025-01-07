def func_1(arr, num):
    for (i, x) in enumerate(arr):
        if x == num:
            return i
    return -1