def count_first_elements(tup):
    count = 0
    for elem in tup:
        if isinstance(elem, tuple):
            break
        count += 1
    return count

# Test cases
assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3
assert count_first_elements((2, 9, (5, 7), 11)) == 2
assert count_first_elements((11, 15, 5, 8, (2, 3), 8)) == 4
