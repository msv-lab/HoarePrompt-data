def get_median(list1, list2, n):
    # Merge the two sorted lists
    merged_list = sorted(list1 + list2)
    
    # Calculate the median
    mid = len(merged_list) // 2
    
    if len(merged_list) % 2 == 0:
        # Even number of elements
        median = (merged_list[mid - 1] + merged_list[mid]) / 2
    else:
        # Odd number of elements (although this case won't happen given the problem constraints)
        median = merged_list[mid]
    
    return median

# Test cases
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
assert get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
assert get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0
