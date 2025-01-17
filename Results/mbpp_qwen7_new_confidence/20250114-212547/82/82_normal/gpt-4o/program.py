def extract_singly(list_of_lists):
    # Use a set comprehension to flatten the list of lists into a single set
    return {element for sublist in list_of_lists for element in sublist}

# Test cases to verify the implementation
assert extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)]) == set([3, 4, 5, 7, 1])
assert extract_singly([(1, 2, 3), (4, 2, 3), (7, 8)]) == set([1, 2, 3, 4, 7, 8])
assert extract_singly([(7, 8, 9), (10, 11, 12), (10, 11)]) == set([7, 8, 9, 10, 11, 12])
