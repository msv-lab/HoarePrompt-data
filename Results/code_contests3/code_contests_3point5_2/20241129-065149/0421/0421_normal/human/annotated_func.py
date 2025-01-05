#State of the program right berfore the function call: n is a positive integer, and ai is a list of integers where each element is between 1 and 100 inclusive.**
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
        
    #State of the program after the loop has been executed: `n` is a positive integer, `ai` is a list of integers where each element is between 1 and 100 inclusive, `flag` is False or True based on the conditions mentioned, `nums` has at least 1 element with the maximum element removed, `i` is equal to len(nums) - 1. If the absolute difference between any elements in `nums` is greater than or equal to 2, `flag` will be set to False and the loop will break. Otherwise, `flag` will retain its previous value
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function `func` reads an integer `n` and a list of integers `ai`, then iterates over the list to check if the absolute difference between any two adjacent elements is less than 2. If this condition holds for all pairs of adjacent elements, it prints 'YES', otherwise 'NO'. The function does not accept any parameters explicitly, instead, it reads input from the user.

