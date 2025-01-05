#State of the program right berfore the function call: n is a positive integer. The array ai contains n positive integers.**
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
        
    #State of the program after the loop has been executed: If there exists at least one pair of elements in `nums` with an absolute difference of 2 or more, `flag` is False; otherwise, `flag` remains True. `nums` is a non-empty list with elements removed based on the conditions specified in the loop.
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function `func` reads a positive integer `n` and an array `ai` containing `n` positive integers. It then iterates through the array elements, checking if there exists a pair with an absolute difference of 2 or more. If such a pair is found, it sets `flag` to False; otherwise, it remains True. The function does not return any specific value but prints 'YES' if flag is True and 'NO' if flag is False.

