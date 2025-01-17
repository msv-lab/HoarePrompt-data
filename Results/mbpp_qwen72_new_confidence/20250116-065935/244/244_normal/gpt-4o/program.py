def find_dissimilar(tup1, tup2):
    set1 = set(tup1)
    set2 = set(tup2)
    dissimilar_elements = set1 ^ set2  # symmetric difference
    return tuple(sorted(dissimilar_elements))

# Test cases
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)
assert find_dissimilar((1, 2, 3, 4), (7, 2, 3, 9)) == (1, 4, 7, 9)
assert find_dissimilar((21, 11, 25, 26), (26, 34, 21, 36)) == (11, 25, 34, 36)
