def last(arr, x):
    # Iterate through the array from the end to the start
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == x:
            return i
    # If the element is not found, return -1 (not specified in tests but good practice)
    return -1

# Tests
assert last([1,2,3],1) == 0
assert last([1,1,1,2,3,4],1) == 2
assert last([2,2,3,3,6,8,9],3) == 3
