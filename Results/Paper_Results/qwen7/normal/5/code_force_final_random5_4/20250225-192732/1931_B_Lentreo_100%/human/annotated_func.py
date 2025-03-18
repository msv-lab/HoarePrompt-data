#State of the program right berfore the function call: nums is a list of integers representing the amounts of water in each container, where the length of nums is n (1 <= n <= 2 * 10^5) and the sum of the integers in nums is divisible by n (1 <= n <= 2 * 10^9).
def func_1(nums):
    n = len(nums)
    total = sum(nums)
    if (total % n != 0) :
        return 'NO'
        #The program returns 'NO'
    #State: `n` is the length of `nums`, `total` is the sum of all elements in `nums`, and `total % n == 0`
    mean = total // n
    curr = 0
    for i in range(n):
        curr += nums[i] - mean
        
        if curr < 0:
            return 'NO'
        
    #State: Output State: `total` is the sum of all elements in `nums`, `n` is the length of `nums`, `total % n == 0`, `mean` is `total // n`, `curr` is the sum of all elements in `nums` minus `n * mean`, `i` is `n`, and if `curr < 0`, the function returns 'NO'. Otherwise, the function continues without returning anything.
    #
    #Explanation: After all iterations of the loop, `curr` will be the sum of all elements in `nums` minus `n * mean`, because each element `nums[i]` is subtracted by `mean` exactly once during the loop. The variable `i` will be equal to `n` since the loop runs from `0` to `n-1`. The function will check if `curr` is less than 0, and if it is, it will return 'NO'. Otherwise, it will continue without returning anything.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function accepts a list of integers `nums` and returns 'NO' if the sum of the integers in `nums` is not divisible by the length of `nums`. Otherwise, it returns 'YES'.

