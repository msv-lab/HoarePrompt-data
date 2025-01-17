def check_min_heap(arr):
    n = len(arr)
    # Iterate over each parent node
    for i in range((n - 2) // 2 + 1):
        # Check left child
        if 2 * i + 1 < n and arr[i] > arr[2 * i + 1]:
            return False
        # Check right child
        if 2 * i + 2 < n and arr[i] > arr[2 * i + 2]:
            return False
    return True

# Test cases
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
assert check_min_heap([2, 10, 4, 5, 3, 15]) == False
