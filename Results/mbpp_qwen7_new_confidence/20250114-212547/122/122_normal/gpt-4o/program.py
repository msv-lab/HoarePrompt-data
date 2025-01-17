def division_elements(tup1, tup2):
    # Perform element-wise division
    result = tuple(a // b for a, b in zip(tup1, tup2))
    return result

# Test cases
assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
assert division_elements((12, 6, 8, 16),(6, 3, 4, 4)) == (2, 2, 2, 4)
assert division_elements((20, 14, 36, 18),(5, 7, 6, 9)) == (4, 2, 6, 2)
