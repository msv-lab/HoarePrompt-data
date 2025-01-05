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
        
    #State of the program after the loop has been executed: Output State: `n` is a string representing the user input, `ai` is a list of positive integers, `flag` is either True or False (based on the absolute differences between consecutive elements in `nums`), `nums` is a list with at least 2 elements where the maximum element has been removed, `i` is len(nums) - 1. The loop will terminate when the flag is set to False or when the nums list is empty.
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function `func` reads the input `n` as a string representing the size of an array and a list of positive integers. It then iterates over the list `nums` and checks if the absolute difference between consecutive elements is less than 2. If the condition is met for all elements, it prints 'YES'; otherwise, it prints 'NO'. The function implicitly assumes the constraints provided for `n` and `ai`. However, the code does not handle invalid inputs, error checking, or edge cases where the list may become empty during execution.

