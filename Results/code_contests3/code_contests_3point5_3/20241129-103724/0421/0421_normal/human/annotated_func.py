#State of the program right berfore the function call: 
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
        
    #State of the program after the loop has been executed: `n` is the user input value, `flag` is False, `nums` is an empty list, `i` is -1
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function `func` reads an input value `n`, then reads a list of integers `nums` from the user. It iterates over `nums` and checks if the absolute difference between consecutive elements is less than 2. If the difference is greater or equal to 2, it sets the `flag` to False and breaks the loop. It then removes the maximum value from `nums`. After the loop, it prints 'YES' if `flag` is True and 'NO' if `flag` is False. The function does not accept any parameters and does not return any value.

