def second_smallest(nums):
    unique_nums = sorted(set(nums))
    return unique_nums[1] if len(unique_nums) > 1 else None

# Test cases
assert second_smallest([1, 2, -8, -2, 0, -2]) == -2
assert second_smallest([1, 1, -0.5, 0, 2, -2, -2]) == -0.5
assert second_smallest([2,2]) == None
assert second_smallest([2,2,2]) == None
