def rotate_right(lst, k):
    n = len(lst)
    k = k % n  # Effective rotation
    return lst[-k:] + lst[:-k]

# Test cases
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) == [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
