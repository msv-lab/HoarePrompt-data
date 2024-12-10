def func_1(nums):
    unique_nums = sorted(set(nums))
    return unique_nums[1] if len(unique_nums) > 1 else None
assert func_1([1, 2, -8, -2, 0, -2]) == -2
assert func_1([1, 1, -0.5, 0, 2, -2, -2]) == -0.5
assert func_1([2, 2]) == None
assert func_1([2, 2, 2]) == None