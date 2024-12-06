def func_1(arr, target):
    (low, high) = (0, len(arr) - 1)
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result
assert func_1([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
assert func_1([2, 3, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 2
assert func_1([1, 2, 4, 5, 6, 6, 8, 9, 9, 9], 6) == 4