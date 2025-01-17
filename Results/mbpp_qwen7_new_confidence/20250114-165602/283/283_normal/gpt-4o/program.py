def move_zero(nums):
    non_zeroes = [num for num in nums if num != 0]
    zeroes = [0] * (len(nums) - len(non_zeroes))
    return non_zeroes + zeroes

# Test cases to verify the function
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
assert move_zero([2,3,2,0,0,4,0,5,0]) == [2,3,2,4,5,0,0,0,0]
assert move_zero([0,1,0,1,1]) == [1,1,1,0,0]
