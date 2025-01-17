def pos_count(nums):
    return len([num for num in nums if num > 0])

# Test cases
assert pos_count([1, -2, 3, -4]) == 2
assert pos_count([3, 4, 5, -1]) == 3
assert pos_count([1, 2, 3, 4]) == 4
