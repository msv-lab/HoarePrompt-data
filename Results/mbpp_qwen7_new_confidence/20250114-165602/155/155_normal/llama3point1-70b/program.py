def max_sum_increasing_subseq(nums, n, k, i):
    max_sum = 0
    for j in range(i, k):
        prev_sum = 0
        for l in range(j):
            if nums[l] < nums[j]:
                prev_sum = max(prev_sum, max_sum_increasing_subseq(nums, n, l, l))
        max_sum = max(max_sum, prev_sum + nums[j])
    return max_sum
