def find_first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            high = mid - 1  # Look on the left side of mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

# Test cases
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
assert find_first_occurrence([2, 3, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 2
assert find_first_occurrence([1, 2, 4, 5, 6, 6, 8, 9, 9, 9], 6) == 4
