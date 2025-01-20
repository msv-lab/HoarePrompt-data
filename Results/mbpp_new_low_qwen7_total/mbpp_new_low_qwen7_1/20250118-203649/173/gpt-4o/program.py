def min_val(lst):
    # Filter out only integer values from the list
    int_values = [x for x in lst if isinstance(x, int)]
    # Find and return the minimum value among the integer values
    return min(int_values)

# Test cases to validate the solution
assert min_val(['Python', 3, 2, 4, 5, 'version']) == 2
assert min_val(['Python', 15, 20, 25]) == 15
assert min_val(['Python', 30, 20, 40, 50, 'version']) == 20
