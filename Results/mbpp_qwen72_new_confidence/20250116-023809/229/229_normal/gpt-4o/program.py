def max_sub_array_sum(arr, n):
    max_so_far = arr[0]
    max_ending_here = arr[0]

    for i in range(1, n):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

# Tests
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
assert max_sub_array_sum([-3, -4, 5, -2, -3, 2, 6, -4], 8) == 8
assert max_sub_array_sum([-4, -5, 6, -3, -4, 3, 7, -5], 8) == 10
