def find_kth(arr1, arr2, k):
    # Merge the two arrays
    merged_array = sorted(arr1 + arr2)
    # Return the k-1 index element since k is 1-based index
    return merged_array[k-1]

# Test cases
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
assert find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7) == 256
assert find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 6) == 8
