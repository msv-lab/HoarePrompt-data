#State of the program right berfore the function call: **
def func():
    n = input()
    flag = True
    nums = map(int, raw_input().split())
    while flag and nums:
        for i in xrange(len(nums) - 1):
            if abs(nums[i] - nums[i + 1]) >= 2:
                flag = False
                break
        
        nums.remove(max(nums))
        
    #State of the program after the loop has been executed: `flag` is True if the absolute difference between any two consecutive elements in `nums` is less than 2, `nums` is a map object containing integers with at least 1 element after removing the maximum element, the loop control variable `i` is the index of the new last element in `nums` - 1
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function `func` reads an integer input `n`, a list of integers `nums`, and checks if the absolute difference between any two consecutive elements in `nums` is less than 2. If this condition holds for all pairs of consecutive elements, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value.

