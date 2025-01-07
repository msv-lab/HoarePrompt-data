def largest_subset(nums):
    if not nums:
        return 0

    nums.sort()
    dp = [1] * len(nums)
    
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Testing the function with the provided test cases
assert largest_subset([1, 3, 6, 13, 17, 18]) == 4
assert largest_subset([10, 5, 3, 15, 20]) == 3
assert largest_subset([18, 1, 3, 6, 13, 17]) == 4
