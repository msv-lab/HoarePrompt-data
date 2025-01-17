def max_of_nth(matrix, n):
    # Extract the nth column (0-indexed)
    nth_column = [row[n] for row in matrix]
    # Return the maximum value from the nth column
    return max(nth_column)

# Test cases
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
assert max_of_nth([[6, 7, 8], [2, 4, 6], [9, 10, 20]], 1) == 10
assert max_of_nth([[7, 8, 9], [3, 5, 7], [10, 11, 21]], 1) == 11
