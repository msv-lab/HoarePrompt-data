from collections import defaultdict

def frequency_lists(list_of_lists):
    # Flatten the list of lists
    flattened_list = [item for sublist in list_of_lists for item in sublist]
    
    # Use defaultdict to count the frequency of each element
    frequency_dict = defaultdict(int)
    for item in flattened_list:
        frequency_dict[item] += 1
    
    return dict(frequency_dict)

# Test cases
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]) == {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
assert frequency_lists([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1}
assert frequency_lists([[20,30,40,17],[18,16,14,13],[10,20,30,40]]) == {20: 2, 30: 2, 40: 2, 17: 1, 18: 1, 16: 1, 14: 1, 13: 1, 10: 1}
