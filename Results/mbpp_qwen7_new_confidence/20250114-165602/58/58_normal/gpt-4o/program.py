def count(bool_list):
    return sum(bool_list)

# Test cases
assert count([True, False, True]) == 2
assert count([False, False]) == 0
assert count([True, True, True]) == 3
