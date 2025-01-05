#State of the program right berfore the function call: n is a positive integer representing the size of the array, and ai is a list of n positive integers where each element represents the height of a stack of ravioli.**
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
        
    #State of the program after the loop has been executed: Output State: `n` is a positive integer, `ai` is a list of positive integers, `flag` is True, `nums` is empty, all elements that were removed from `nums` had an absolute difference of less than 2 with their adjacent elements in the list.
    print['NO', 'YES'][flag]
#Overall this is what the function does:The `func` function implicitly accepts a positive integer `n` representing the size of an array and a list `ai` of `n` positive integers representing the height of a stack of ravioli. The function then reads input, processes the heights of the ravioli stacks, and determines whether the absolute difference between adjacent elements is less than 2. If the condition holds for all elements, it prints 'YES'; otherwise, it prints 'NO'.

