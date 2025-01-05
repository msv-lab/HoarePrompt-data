#State of the program right berfore the function call: The function does not take any parameters, but the input consists of an integer n (1 ≤ n ≤ 10) followed by n space-separated integers ai (1 ≤ ai ≤ 100) representing the elements of the array.
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
        
    #State of the program after the loop has been executed: `n` is a non-empty string, `flag` is False if any absolute difference between consecutive elements in `nums` was greater than or equal to 2 during the iterations, otherwise `flag` is True; `nums` is a non-empty list containing the remaining elements after repeatedly removing the maximum value until no further removals can be made.
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function accepts no parameters but reads an integer `n` followed by `n` space-separated integers. It checks if the absolute difference between any two consecutive integers in the list is less than 2. If such a difference is found, the function sets a flag to False. It also repeatedly removes the maximum value from the list until no further removals can be made. Finally, it prints 'YES' if the flag remains True (indicating all consecutive differences were less than 2) and 'NO' otherwise. Note that the function does not handle cases where the input is invalid or where `n` is outside the specified range.

