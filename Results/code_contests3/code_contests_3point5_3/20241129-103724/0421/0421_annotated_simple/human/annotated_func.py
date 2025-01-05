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
        
    #State of the program after the loop has been executed: n` is a positive integer, `ai` contains n positive integers, `flag` is either True or False (based on the absolute difference between consecutive elements in the updated `nums` list), `nums` is not empty (with all elements that have an absolute difference greater than or equal to 2 removed), `i` is len(nums) - 2
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function `func` reads a positive integer `n`, followed by a list of positive integers `nums`. It then iterates through the list, removing elements with an absolute difference of 2 or more from their neighbors until no such elements exist. Finally, it prints either 'YES' or 'NO' based on the value of the flag variable. The code does not return a list of positive integers in reverse order as indicated in the annotations.

