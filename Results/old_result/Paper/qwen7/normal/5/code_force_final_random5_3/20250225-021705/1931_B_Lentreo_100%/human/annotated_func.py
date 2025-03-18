#State of the program right berfore the function call: nums is a list of integers representing the amounts of water in each container, where the length of nums is n (1 <= n <= 2 * 10^5) and the sum of the elements in nums is divisible by n (1 <= n).
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
        
    #State: Output State: After the loop executes all the iterations, `i` is `n`, `curr` is the sum of the differences between each element in `nums` and the mean (`total // n`), and `curr` is greater than or equal to 0.
    #
    #In more detail, `i` will be equal to the length of `nums` (denoted as `n`), because the loop runs from `0` to `n-1`. The variable `curr` accumulates the sum of `nums[i] - mean` for each iteration of the loop. If at any point during these iterations, `curr` becomes less than 0, the function would return 'NO' immediately. Since we are considering the state after all iterations, it means that `curr` never became negative, and thus the function would return 'YES' (implied by the absence of a return statement before the end of the loop).
    return 'YES'
    #The program returns 'YES', indicating that the sum of the differences between each element in `nums` and the mean (`total // n`) is always greater than or equal to 0 after all iterations.
#Overall this is what the function does:The function accepts a list of integers `nums`. It calculates the mean value based on the sum of the elements in `nums` divided by the length of `nums`. It then checks if the cumulative sum of the differences between each element in `nums` and the mean remains non-negative throughout the iteration. If the cumulative sum ever becomes negative, the function returns 'NO'. Otherwise, it returns 'YES', indicating that the sum of the differences between each element in `nums` and the mean is always greater than or equal to 0.

