#State of the program right berfore the function call: n is a positive integer representing the size of the array, and ai is a list of n positive integers where each integer represents the height of a stack of ravioli.**
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
        
    #State of the program after the loop has been executed: `n` is a positive integer, `ai` is a list of n positive integers, `flag` is True, `nums` is an empty list, the loop did not execute as nums became empty before the loop condition check
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function `func` reads an input integer `n` representing the size of an array and a list of positive integers `ai` representing the height of a stack of ravioli. It then iterates through the list checking if the absolute difference between consecutive elements is greater than or equal to 2. If such a difference is found, it sets the flag to False and exits the loop. After the loop, it removes the maximum element from the list `nums`. Finally, it prints 'YES' if the flag is True (meaning all height differences are less than 2) and 'NO' if the flag is False.

