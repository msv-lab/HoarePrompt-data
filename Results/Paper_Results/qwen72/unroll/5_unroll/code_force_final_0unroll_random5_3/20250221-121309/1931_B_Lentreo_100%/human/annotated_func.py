#State of the program right berfore the function call: nums is a list of integers where the sum of the integers is divisible by the length of the list.
def func_1(nums):
    n = len(nums)
    total = sum(nums)
    if (total % n != 0) :
        return 'NO'
        #The program returns 'NO'
    #State: `nums` is a list of integers where the sum of the integers is divisible by the length of the list, `n` is the length of `nums`, `total` is the sum of the integers in `nums`, and `total % n` is equal to 0.
    mean = total // n
    curr = 0
    for i in range(n):
        curr += nums[i] - mean
        
        if curr < 0:
            return 'NO'
        
    #State: `curr` is 0, `n` and `mean` remain unchanged, `total` remains unchanged.
    return 'YES'
    #The program returns 'YES'.
#Overall this is what the function does:The function `func_1` accepts a list of integers `nums` where the sum of the integers is divisible by the length of the list. It checks if the list can be balanced such that the cumulative difference from the mean of the list never becomes negative. If the list cannot be balanced, it returns 'NO'. If the list can be balanced, it returns 'YES'.

