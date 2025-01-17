def odd_length_sum(nums):
    total_sum = 0
    n = len(nums)
    for length in range(1, n + 1):
        if length % 2 != 0:
            for i in range(n - length + 1):
                total_sum += sum(nums[i:i + length])
    return total_sum
