def sum_even_and_even_index(lst):
    return sum(value for index, value in enumerate(lst) if index % 2 == 0 and value % 2 == 0)

# Test cases to verify the function
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
assert sum_even_and_even_index([3, 20, 17, 9, 2, 10, 18, 13, 6, 18]) == 26
assert sum_even_and_even_index([5, 6, 12, 1]) == 12
