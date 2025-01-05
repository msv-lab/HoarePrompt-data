#State of the program right berfore the function call: The input consists of an integer n (1 ≤ n ≤ 10), followed by n space-separated integers ai (1 ≤ ai ≤ 100), where ai represents the height of the stacks of ravioli.
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
        
    #State of the program after the loop has been executed: `n` is an input string representing an integer; `flag` is False if there exists any pair of consecutive integers in `nums` with an absolute difference of 2 or more; otherwise, `flag` is True; `nums` is empty after all maximum integers have been removed.
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 10) followed by `n` space-separated integers representing the heights of stacks of ravioli. It checks if there are any consecutive heights that differ by 2 or more; if such a pair exists, it prints 'NO', otherwise it prints 'YES'. The function continues to check until all maximum heights have been removed, but if there are only two heights, it does not handle the case correctly, potentially missing some conditions.

