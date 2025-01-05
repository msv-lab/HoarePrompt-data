#State of the program right berfore the function call: n is a positive integer and ai contains n positive integers.**
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
        
    #State of the program after the loop has been executed: `n` is a string, `ai` contains `n` positive integers, `flag` is False, `nums` contains at least 2 elements after removal of the maximum value. The loop will not execute again.
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function `func` reads an integer `n` and a list of integers `nums`. It then iterates through the list checking if the absolute difference between consecutive elements is less than 2. If it finds a difference greater than or equal to 2, it sets the `flag` to False and stops the iteration. It then removes the maximum value from `nums`. Finally, it prints 'YES' if `flag` is True, and 'NO' otherwise. The function does not explicitly return a value.

