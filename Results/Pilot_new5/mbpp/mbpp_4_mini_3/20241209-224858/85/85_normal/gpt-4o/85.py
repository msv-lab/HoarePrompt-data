def max_Abs_Diff(arr):
    # Find the minimum and maximum values in the array
    min_val = min(arr)
    max_val = max(arr)
    
    # Calculate the maximum absolute difference
    max_diff = max_val - min_val
    
    return max_diff

# Test cases
assert max_Abs_Diff((2, 1, 5, 3)) == 4
assert max_Abs_Diff((9, 3, 2, 5, 1)) == 8
assert max_Abs_Diff((3, 2, 1)) == 2
