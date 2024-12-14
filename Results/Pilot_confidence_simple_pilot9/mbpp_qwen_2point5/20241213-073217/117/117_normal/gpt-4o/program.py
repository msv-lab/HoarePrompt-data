def count_integer(lst):
    return sum(1 for x in lst if isinstance(x, int))

# Provided test cases
assert count_integer([1, 2, 'abc', 1.2]) == 2
assert count_integer([1, 2, 3]) == 3
assert count_integer([1, 1.2, 4, 5.1]) == 2
