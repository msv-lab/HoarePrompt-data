import math

def zero_count(arr):
    zeroes = arr.count(0)
    non_zeroes = len(arr) - zeroes
    
    if non_zeroes == 0:
        return float('inf')  # To handle division by zero if there are no non-zero elements
    
    return zeroes / non_zeroes

# Test cases
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
assert math.isclose(zero_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]), 0.00, rel_tol=0.001)
assert math.isclose(zero_count([2, 4, -6, -9, 11, -12, 14, -5, 17]), 0.00, rel_tol=0.001)
