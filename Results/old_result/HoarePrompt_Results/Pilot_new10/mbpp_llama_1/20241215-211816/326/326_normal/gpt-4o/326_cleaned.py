def func_1(arr, n):
    if n < 2:
        return 0
    arr = sorted(arr)
    min_diff = float('inf')
    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff
assert func_1((1, 5, 3, 19, 18, 25), 6) == 1
assert func_1((4, 3, 2, 6), 4) == 1
assert func_1((30, 5, 20, 9), 4) == 4