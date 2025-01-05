#State of the program right berfore the function call: The input consists of an integer n (1 ≤ n ≤ 10), followed by n space-separated integers ai (1 ≤ ai ≤ 100), representing the elements of the array.
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
        
    #State of the program after the loop has been executed: `n` is a non-empty string containing at least one integer; `flag` is False if any adjacent elements in `nums` have an absolute difference of 2 or more, otherwise `flag` is True; `nums` is empty after all maximum values have been removed.
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function accepts an integer `n` followed by `n` space-separated integers. It checks whether the absolute difference between any two adjacent integers in the list is less than 2. If such a difference is found, it sets a flag to False. The function continues to remove the maximum value from the list until it becomes empty. Finally, it prints 'YES' if no adjacent integers had an absolute difference of 2 or more, otherwise it prints 'NO'. Note that the function does not handle cases where `n` is not provided or the input format is incorrect.

