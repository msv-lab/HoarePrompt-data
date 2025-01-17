def pair_xor_Sum(nums, n):
    xor_sum = 0
    for i in range(n):
        for j in range(i + 1, n):
            xor_sum += nums[i] ^ nums[j]
    return xor_sum

# Test cases
assert pair_xor_Sum([5, 9, 7, 6], 4) == 47
assert pair_xor_Sum([7, 3, 5], 3) == 12
assert pair_xor_Sum([7, 3], 2) == 4
