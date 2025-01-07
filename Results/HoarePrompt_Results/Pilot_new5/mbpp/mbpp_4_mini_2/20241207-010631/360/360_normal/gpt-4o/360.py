def max_sum_list(list_of_lists):
    # Initialize variables to track the maximum sum and the corresponding list
    max_sum = float('-inf')
    max_list = []
    
    # Iterate through each sublist
    for sublist in list_of_lists:
        # Calculate the sum of the current sublist
        current_sum = sum(sublist)
        
        # If the current sum is greater than the maximum sum found so far
        if current_sum > max_sum:
            # Update the maximum sum and the corresponding list
            max_sum = current_sum
            max_list = sublist
    
    # Return the list with the highest sum
    return max_list

# Tests
assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]) == [10, 11, 12]
assert max_sum_list([[3,2,1], [6,5,4], [12,11,10]]) == [12, 11, 10]
assert max_sum_list([[2,3,1]]) == [2, 3, 1]
