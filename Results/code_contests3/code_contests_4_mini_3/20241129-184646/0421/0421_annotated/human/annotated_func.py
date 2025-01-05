#State of the program right berfore the function call: The input consists of an integer n (1 ≤ n ≤ 10) representing the size of the array, followed by n space-separated integers ai (1 ≤ ai ≤ 100) that represent the heights of the stacks of ravioli.
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
        
    #State of the program after the loop has been executed: `n` is an integer greater than or equal to 0, `flag` is False if any absolute difference between consecutive elements in `nums` is greater than or equal to 2 at any point during the loop execution, otherwise `flag` is True, `i` is undefined as the loop has finished executing, and `nums` is an empty list if the loop executed at least once and all elements were removed, or a list with at least 0 elements remaining after the maximum elements were removed until the stopping condition was met.
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 10) representing the number of stacks of ravioli, followed by `n` space-separated integers representing the heights of the stacks. It checks if the absolute difference between the heights of any two consecutive stacks is less than 2. If such a difference is found, it sets a flag to False. The function repeatedly removes the maximum height stack until either all stacks are removed or a stack difference condition fails. Finally, it prints 'YES' if the flag remains True, indicating all conditions were met, or 'NO' if the flag is False, indicating a condition was breached. Note that if there are fewer than 2 stacks, the function will always print 'YES' since the loop will not execute.

