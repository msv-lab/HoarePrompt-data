def tuple_to_dict(tup):
    # Initialize an empty dictionary
    result = {}
    
    # Iterate through the tuple in steps of 2
    for i in range(0, len(tup), 2):
        # Add the adjacent elements to the dictionary
        result[tup[i]] = tup[i + 1]
    
    return result

# Test cases to validate the solution
assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
assert tuple_to_dict((1, 2, 3, 4, 5, 6)) == {1: 2, 3: 4, 5: 6}
assert tuple_to_dict((7, 8, 9, 10, 11, 12)) == {7: 8, 9: 10, 11: 12}
