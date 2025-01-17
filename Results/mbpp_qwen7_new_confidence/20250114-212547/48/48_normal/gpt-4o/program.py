def Find_Min_Length(list_of_lists):
    # Initialize the minimum length to a very large number
    min_length = float('inf')
    
    # Iterate over each sublist in the list of lists
    for sublist in list_of_lists:
        # Update the minimum length if the current sublist is shorter
        if len(sublist) < min_length:
            min_length = len(sublist)
    
    return min_length

# Test cases
assert Find_Min_Length([[1],[1,2]]) == 1
assert Find_Min_Length([[1,2],[1,2,3],[1,2,3,4]]) == 2
assert Find_Min_Length([[3,3,3],[4,4,4,4]]) == 3
