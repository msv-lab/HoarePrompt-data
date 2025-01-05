#State of the program right berfore the function call: n is a positive integer, and ai is a list of n positive integers.**
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
        
    #State of the program after the loop has been executed: `n` is a positive integer, `ai` is a list of n positive integers, `flag` is False if there exists a pair of adjacent elements in `nums` with an absolute difference of at least 2, `nums` has a length of 0, and `i` is len(nums) - 2
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function `func` reads a positive integer `n` and a list of `n` positive integers `ai`. It then iterates through the elements of `ai`, checking if there exists a pair of adjacent elements with an absolute difference of at least 2. If such a pair is found, it sets the flag to False and stops the iteration. Finally, it prints 'YES' if no such pair is found, and 'NO' otherwise. However, the function lacks a return statement, so it does not explicitly return any value.

