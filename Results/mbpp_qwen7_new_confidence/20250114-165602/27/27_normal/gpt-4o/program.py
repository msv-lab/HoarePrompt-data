def is_Monotonic(arr):
    if all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)):
        return True
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        return True
    return False

# Tests
assert is_Monotonic([6, 5, 4, 4]) == True
assert is_Monotonic([1, 2, 2, 3]) == True
assert is_Monotonic([1, 3, 2]) == False
