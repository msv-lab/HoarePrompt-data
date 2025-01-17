def move_zero(nums):
    return [num for num in nums if num != 0] + [num for num in nums if num == 0]
