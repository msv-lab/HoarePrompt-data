#State of the program right berfore the function call: The input consists of an integer n (1 ≤ n ≤ 10) indicating the size of the array, followed by n space-separated integers ai (1 ≤ ai ≤ 100) representing the elements of the array.
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
        
    #State of the program after the loop has been executed: `n` is an integer; `flag` is True if all consecutive elements in `nums` have an absolute difference of less than 2; otherwise, `flag` is False; `nums` is empty after all maximum values have been removed.
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function reads an integer `n` (1 ≤ n ≤ 10) and `n` space-separated integers `ai` (1 ≤ ai ≤ 100) representing the elements of an array. It checks if all consecutive elements in the array have an absolute difference of less than 2. If any such difference is found, the function sets a flag to False; otherwise, the flag remains True. After iterating through the array and removing the maximum value repeatedly until the array is empty, it prints 'YES' if the flag is still True (indicating all consecutive elements had an absolute difference of less than 2) or 'NO' if the flag is False at any point. Note that the function does not return any values but prints the result directly.

