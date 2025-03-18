#State of the program right berfore the function call: nums is a list of integers where the sum of the integers is divisible by the length of the list (len(nums)).
def func_1(nums):
    n = len(nums)
    total = sum(nums)
    if (total % n != 0) :
        return 'NO'
        #The program returns 'NO'
    #State: *`nums` is a list of integers where the sum of the integers is divisible by the length of the list (len(nums)), `n` is equal to the length of `nums`, `total` is the sum of the integers in `nums`, and the sum of the integers in `nums` is divisible by `n` (i.e., `total % n == 0`)
    mean = total // n
    curr = 0
    for i in range(n):
        curr += nums[i] - mean
        
        if curr < 0:
            return 'NO'
        
    #State: `curr` is 0, `nums` remains unchanged, `n` remains unchanged, `total` remains unchanged, `mean` remains unchanged.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` accepts a list of integers `nums` where the sum of the integers is divisible by the length of the list. It checks if the cumulative deviation from the mean of the list, calculated as the sum of the integers divided by the length of the list, ever becomes negative. If at any point the cumulative deviation is negative, the function returns 'NO'. If the cumulative deviation never becomes negative, the function returns 'YES'. The list `nums` remains unchanged after the function execution.

