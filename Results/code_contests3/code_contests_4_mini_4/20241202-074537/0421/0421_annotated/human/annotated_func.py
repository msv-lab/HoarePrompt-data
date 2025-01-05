#State of the program right berfore the function call: The input consists of an integer n (1 ≤ n ≤ 10) representing the size of the array, followed by n space-separated integers ai (1 ≤ ai ≤ 100) that represent the elements of the array.
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
        
    #State of the program after the loop has been executed: `n` is a valid input string that generates at least one integer in `nums`; `flag` is False if any two consecutive integers in `nums` have an absolute difference of 2 or more; otherwise, `flag` is True; `nums` is empty after all maximum values have been removed.
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function accepts an integer `n` representing the size of the array, followed by `n` space-separated integers. It checks if any two consecutive integers in the list have an absolute difference of 2 or more. If such a pair exists, it outputs 'NO'; otherwise, it outputs 'YES'. The function continuously removes the maximum value from the list until it is empty or the condition is violated. However, there is a missing check for the case when `n` is 0, which is not handled as the input constraints indicate that `n` will always be between 1 and 10. Therefore, the function assumes valid input without error handling for invalid cases.

