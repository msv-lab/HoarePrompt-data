def search(arr):
    if not arr:
        return None  # If the array is empty, return None
    
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        # Check if the mid is even or odd
        if mid % 2 == 1:
            mid -= 1
        
        # Compare mid with the next element
        if arr[mid] == arr[mid + 1]:
            left = mid + 2
        else:
            right = mid
    
    return arr[left]

# Test cases
assert search([1,1,2,2,3]) == 3
assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
assert search([1,2,2,3,3,4,4]) == 1
