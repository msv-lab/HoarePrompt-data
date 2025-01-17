def sum_in_range(l, r):
    return sum(i for i in range(l, r + 1) if i % 2 != 0)

# Test cases
assert sum_in_range(2, 5) == 8
assert sum_in_range(5, 7) == 12
assert sum_in_range(7, 13) == 40
