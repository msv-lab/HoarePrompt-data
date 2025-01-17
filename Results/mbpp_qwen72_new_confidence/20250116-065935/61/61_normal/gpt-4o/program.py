def common_in_nested_lists(nested_lists):
    # Convert the first list to a set
    common_elements = set(nested_lists[0])
    
    # Iterate through the remaining lists and intersect with the current set of common elements
    for lst in nested_lists[1:]:
        common_elements &= set(lst)
    
    # Return the common elements as a list
    return list(common_elements)

# Test cases
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]])) == set([18, 12])
assert set(common_in_nested_lists([[12, 5, 23, 25, 45], [7, 11, 5, 23, 28], [1, 5, 8, 18, 23, 16]])) == set([5, 23])
assert set(common_in_nested_lists([[2, 3, 4, 1], [4, 5], [6, 4, 8], [4, 5], [6, 8, 4]])) == set([4])
