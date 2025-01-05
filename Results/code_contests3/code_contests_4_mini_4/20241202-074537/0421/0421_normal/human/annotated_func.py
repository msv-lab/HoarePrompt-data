#State of the program right berfore the function call: The input consists of an integer n (1 ≤ n ≤ 10) representing the size of the array, followed by n space-separated integers ai (1 ≤ ai ≤ 100) which represent the elements of the array.
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
        
    #State of the program after the loop has been executed: `n` is an input string representing the size of the array; `flag` is False if there exists at least one pair of adjacent elements in `nums` with an absolute difference of 2 or more, otherwise `flag` is True; `nums` is empty after all maximum values have been removed from the original array.
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 10) followed by `n` space-separated integers (1 ≤ ai ≤ 100). It checks if any adjacent pair of numbers in the list has an absolute difference of 2 or more. If such a pair exists, it returns 'NO'; otherwise, it returns 'YES'. The function continues checking until the list is empty, removing the maximum value in each iteration. However, the result may not accurately reflect all pairs due to the removal of maximum values and may not handle cases where there are fewer than two elements properly.

