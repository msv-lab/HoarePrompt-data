#State of the program right berfore the function call: n is a positive integer representing the size of the array. ai is a list of n positive integers where each integer represents the height of the stack of ravioli.**
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
        
    #State of the program after the loop has been executed: n is a positive integer, ai is a list of n positive integers, flag is False or remains True based on the modified nums list, nums is not empty, i is either 0 or len(nums) - 1. The loop removes the maximum element from nums each iteration and updates flag based on the presence of adjacent numbers in nums with an absolute difference of at least 2.
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function `func` reads an integer `n` representing the size of an array and a list of `n` positive integers `ai` representing the height of a stack of ravioli. It then iterates over the list `ai`, removing the maximum element each iteration, and updates a flag based on the absolute difference of adjacent numbers. Finally, it prints 'YES' if the flag is True, indicating the stack is stable, and 'NO' if the flag is False, indicating the stack is not stable. However, the function lacks explicit parameter handling and return statements based on the annotations provided.

