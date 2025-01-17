def max_val(lst):
    # Filter only numeric values from the list
    numeric_values = [x for x in lst if isinstance(x, (int, float))]
    # Return the maximum value among the numeric values
    return max(numeric_values)

# Test cases
assert max_val(['Python', 3, 2, 4, 5, 'version']) == 5
assert max_val(['Python', 15, 20, 25]) == 25
assert max_val(['Python', 30, 20, 40, 50, 'version']) == 50
