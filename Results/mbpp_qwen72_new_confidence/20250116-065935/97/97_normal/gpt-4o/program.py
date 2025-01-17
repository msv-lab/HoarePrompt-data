def is_majority(arr, n, x):
    # Helper function to find the first occurrence of x in arr
    def first_occurrence(arr, n, x):
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
                return mid
            elif x > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    
    # Helper function to find the last occurrence of x in arr
    def last_occurrence(arr, n, x):
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if (mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x:
                return mid
            elif x < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    
    # Find the first and last occurrence of x
    first = first_occurrence(arr, n, x)
    if first == -1:
        return False  # x is not present in the array
    
    last = last_occurrence(arr, n, x)
    
    # Calculate the count of x in the array
    count = last - first + 1
    
    # Check if count is greater than n / 2
    return count > n // 2

# Test cases
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
