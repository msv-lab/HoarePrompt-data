#State of the program right berfore the function call: The input consists of an integer n (1 ≤ n ≤ 10) representing the size of the array, followed by n space-separated integers ai (1 ≤ ai ≤ 100) which represent the heights of the stacks.
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
        
    #State of the program after the loop has been executed: `n` is a string representing a valid integer, `flag` is False if any absolute difference between consecutive elements of `nums` is greater than or equal to 2 during any iteration, otherwise `flag` is True; `nums` is an empty list after all maximum values have been successively removed.
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function accepts an integer `n` representing the size of an array and then `n` space-separated integers representing the heights of the stacks. It checks if the absolute difference between any two consecutive heights is less than 2. If any difference is 2 or more, it sets a flag to False. The function removes the maximum height from the list iteratively until the list is empty or the flag is set to False. Finally, it prints 'YES' if the flag remains True (indicating all differences were within the acceptable range) and 'NO' otherwise.

