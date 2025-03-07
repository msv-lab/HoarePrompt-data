#State of the program right berfore the function call: nums is a list of integers where the sum of the integers is divisible by the length of the list.
def func_1(nums):
    n = len(nums)
    total = sum(nums)
    if (total % n != 0) :
        return 'NO'
        #The program returns 'NO'
    #State: `nums` is a list of integers where the sum of the integers is divisible by the length of the list, `n` is equal to the length of `nums`, `total` is the sum of the integers in `nums`, and `total % n` is equal to 0.
    mean = total // n
    curr = 0
    for i in range(n):
        curr += nums[i] - mean
        
        if curr < 0:
            return 'NO'
        
    #State: `curr` is 0, `nums` is unchanged, `n` is unchanged, `total` is unchanged, `mean` is unchanged.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` accepts a list of integers `nums` where the sum of the integers is divisible by the length of the list. It checks whether it is possible to make all elements in the list equal to the mean of the list by only adding or subtracting the same value from each element. If at any point during the check, the cumulative deviation from the mean becomes negative, the function returns 'NO'. If the cumulative deviation remains non-negative throughout the check, the function returns 'YES'. The function does not modify the input list `nums`.

