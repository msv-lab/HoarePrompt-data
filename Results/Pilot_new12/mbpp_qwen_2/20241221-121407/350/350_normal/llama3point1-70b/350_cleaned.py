def func_1(arr, target):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i
    return -1