def sequential_search(arr, element):
    for index, value in enumerate(arr):
        if value == element:
            return (True, index)
    return (False, -1)

# Test cases
assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
assert sequential_search([12, 32, 45, 62, 35, 47, 44, 61],61) == (True, 7)
assert sequential_search([9, 10, 17, 19, 22, 39, 48, 56],48) == (True, 6)
