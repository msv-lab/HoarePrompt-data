def find_min_diff(arr, target):
    arr = sorted(arr)
    min_diff = float('inf')
    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i + 1])
        if diff < min_diff:
            min_diff = diff
    return min_diff
