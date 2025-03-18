#State of the program right berfore the function call: nums is a list of integers representing the amounts of water in each container, where the length of nums is n (1 <= n <= 2 * 10^5) and the sum of nums is divisible by n (1 <= n <= 2 * 10^9).
def func_1(nums):
    n = len(nums)
    total = sum(nums)
    if (total % n != 0) :
        return 'NO'
        #The program returns 'NO'
    #State: `n` is the length of `nums`, and the sum of `nums` is divisible by `n`, `total` is the sum of `nums`. The sum of `nums` is divisible by `n`
    mean = total // n
    curr = 0
    for i in range(n):
        curr += nums[i] - mean
        
        if curr < 0:
            return 'NO'
        
    #State: Output State: `curr` is the sum of elements in `nums` each subtracted by `mean`, and either `'NO'` is returned if `curr` becomes less than 0 at any point during the loop iterations or the loop completes without returning anything, meaning `curr` is non-negative after all iterations.
    return 'YES'
    #'YES'
#Overall this is what the function does:The function accepts a list of integers `nums` representing the amounts of water in each container. It calculates the mean amount of water per container. If at any point during the iteration, the cumulative difference between the current sum of `nums` and the mean becomes negative, it returns 'NO', indicating that equal distribution is not possible. If the loop completes without returning 'NO', it returns 'YES', indicating that the water can be distributed equally among the containers.

