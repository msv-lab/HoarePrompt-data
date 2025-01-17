def max_sub_array_sum_repeated(arr, n, k):
    def kadane(arr):
        max_ending_here = max_so_far = arr[0]
        for x in arr[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
    
    max_kadane = kadane(arr)
    if k == 1:
        return max_kadane
    
    max_prefix_sum = max_suffix_sum = float('-inf')
    current_prefix_sum = 0
    current_suffix_sum = 0
    total_sum = 0
    
    for i in range(n):
        total_sum += arr[i]
        current_prefix_sum += arr[i]
        max_prefix_sum = max(max_prefix_sum, current_prefix_sum)
        
    for i in range(n-1, -1, -1):
        current_suffix_sum += arr[i]
        max_suffix_sum = max(max_suffix_sum, current_suffix_sum)
    
    if total_sum > 0:
        return max(max_kadane, max_prefix_sum + max_suffix_sum + (k - 2) * total_sum)
    else:
        return max(max_kadane, max_prefix_sum + max_suffix_sum)

# Test cases
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1
