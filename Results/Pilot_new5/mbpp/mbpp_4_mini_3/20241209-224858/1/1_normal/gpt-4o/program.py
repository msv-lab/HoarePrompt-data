def similar_elements(list1, list2):
    # Convert both lists to sets and find their intersection
    common_elements = set(list1) & set(list2)
    # Convert the result back to a tuple and return
    return tuple(sorted(common_elements))

# Test cases
assert similar_elements((3, 4, 5, 6), (5, 7, 4, 10)) == (4, 5)
assert similar_elements((1, 2, 3, 4), (5, 4, 3, 7)) == (3, 4)
assert similar_elements((11, 12, 14, 13), (17, 15, 14, 13)) == (13, 14)
