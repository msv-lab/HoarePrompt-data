#State of the program right berfore the function call: n is a positive integer, and ai is a list of integers where 1 ≤ ai ≤ 100 for each element in the list.**
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
        
    #State of the program after the loop has been executed: n is a positive integer, ai is a list of integers where 1 ≤ ai ≤ 100 for each element, flag is False if there exists at least one pair of elements in nums with an absolute difference of 2 or more, nums is a list of integers with the maximum value removed
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function `func` reads a positive integer `n` and a list of integers `ai` from input. It iterates over the list `ai` and checks if there exists a pair of elements with an absolute difference of 2 or more. If such a pair is found, it sets `flag` to False. It then removes the maximum value from the list `ai`. Finally, it prints 'YES' if `flag` is True, meaning no pair with an absolute difference of 2 or more was found, and 'NO' otherwise.

