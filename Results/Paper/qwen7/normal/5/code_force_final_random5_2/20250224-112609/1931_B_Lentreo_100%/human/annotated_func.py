#State of the program right berfore the function call: nums is a list of integers representing the amounts of water in each container, where the length of nums is n (1 <= n <= 2 * 10^5) and the sum of nums is divisible by n (1 <= n <= 2 * 10^5), with each element in nums being in the range 0 <= a_i <= 10^9.
def func_1(nums):
    n = len(nums)
    total = sum(nums)
    if (total % n != 0) :
        return 'NO'
        #The program returns 'NO'
    mean = total // n
    curr = 0
    for i in range(n):
        curr += nums[i] - mean
        
        if curr < 0:
            return 'NO'
        
    #State: Output State: `total` is equal to the sum of `nums`, `n` is the length of `nums` and must be greater than 0, the sum of `nums` is divisible by `n`, `mean` is `total` // `n`, `curr` is the sum of `nums[i] - mean` for all `i` from 0 to `n-1`, `i` is `n`, and if `curr` is less than 0 at any point during the loop, the function returns 'NO'. If the loop completes without returning 'NO', then `curr` will be 0 because the sum of all `nums[i] - mean` will cancel out to zero.
    #
    #This means that after all iterations of the loop, `curr` will be 0 (since the sum of deviations from the mean over all elements must balance out to zero), `i` will be equal to `n` (indicating the loop has completed all iterations), and the function will not have returned 'NO' unless `curr` went below 0 at some point during the loop.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function accepts a list of integers `nums` representing the amounts of water in each container. It calculates the mean amount of water per container and checks if the cumulative deviation from the mean remains non-negative throughout the iteration. If the cumulative deviation ever becomes negative or the total sum of `nums` is not divisible by its length, the function returns 'NO'. Otherwise, it returns 'YES', indicating that the cumulative deviation from the mean balances out to zero.

