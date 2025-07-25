def substract_elements(tup1, tup2):
    return tuple(a - b for a, b in zip(tup1, tup2))

# Test cases
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
assert substract_elements((11, 2, 3), (24, 45 ,16)) == (-13, -43, -13)
assert substract_elements((7, 18, 9), (10, 11, 12)) == (-3, 7, -3)
