#State of the program right berfore the function call: nums is a list of non-negative integers where the sum of the elements in nums is divisible by the length of nums.
def func_1(nums):
    n = len(nums)
    total = sum(nums)
    if (total % n != 0) :
        return 'NO'
        #The program returns 'NO'
    #State: `nums` is a list of non-negative integers where the sum of the elements in `nums` is divisible by the length of `nums`, `n` is the length of `nums`, `total` is the sum of the elements in `nums`, and the sum of the elements in `nums` is exactly divisible by `n` (i.e., `total % n == 0`).
    mean = total // n
    curr = 0
    for i in range(n):
        curr += nums[i] - mean
        
        if curr < 0:
            return 'NO'
        
    #State: `nums` is a list of non-negative integers where the sum of the elements in `nums` is divisible by the length of `nums`, `n` is the length of `nums`, `total` is the sum of the elements in `nums`, `mean` is the integer division of `total` by `n` (i.e., `mean = total // n`), `curr` is the sum of `(nums[i] - mean)` for all `i` from 0 to `n-1`, and `i` is `n-1`. If `curr` is less than 0 at any point during the loop, the function returns 'NO'. Otherwise, the function completes the loop with `curr` equal to 0.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` accepts a list of non-negative integers `nums` where the sum of the elements in `nums` is divisible by the length of the list. It returns 'NO' if the sum of the deviations of the elements from the mean (calculated as the integer division of the total sum by the length of the list) is negative at any point during the iteration through the list. If the sum of the deviations remains non-negative throughout the iteration, the function returns 'YES'.

