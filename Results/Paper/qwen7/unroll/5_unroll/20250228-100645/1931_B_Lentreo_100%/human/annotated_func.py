#State of the program right berfore the function call: nums is a list of integers representing the amounts of water in each container, where the length of nums is n (1 ≤ n ≤ 2⋅10^5) and the sum of the elements in nums is divisible by n (1 ≤ n ≤ 2⋅10^9).
def func_1(nums):
    n = len(nums)
    total = sum(nums)
    if (total % n != 0) :
        return 'NO'
        #The program returns 'NO'
    #State: `n` is the length of `nums`, and the sum of the elements in `nums` is divisible by `n`; `total` is the sum of the elements in `nums`. The total sum of the elements in `nums` is divisible by `n`.
    mean = total // n
    curr = 0
    for i in range(n):
        curr += nums[i] - mean
        
        if curr < 0:
            return 'NO'
        
    #State: Output State: `n` is the length of `nums`, the sum of the elements in `nums` is divisible by `n`; `total` is the sum of the elements in `nums`, `mean` is the integer division of `total` by `n`, `curr` is 0.
    #
    #Explanation: The loop iterates over each element in `nums`, updating `curr` by adding the difference between the current element and the mean to `curr`. If at any point `curr` becomes less than 0, the function returns 'NO'. However, since the sum of the elements in `nums` is divisible by `n`, and `curr` starts at 0, it will never go negative because each addition of `(nums[i] - mean)` will either keep `curr` at 0 or make it positive (since `nums[i] - mean` can be negative but the sum of these differences over all elements will balance out to 0 due to the divisibility condition). Therefore, the loop completes without returning 'NO', and `curr` remains 0.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function accepts a list of integers `nums` representing the amounts of water in each container. It checks if the water can be distributed equally among the containers. If the total amount of water is not divisible by the number of containers, it returns 'NO'. Otherwise, it iterates through the list, calculating the difference between each container's water amount and the average water amount, ensuring the cumulative difference does not become negative. If the cumulative difference remains non-negative throughout the iteration, it returns 'YES', indicating equal distribution is possible; otherwise, it returns 'NO'.

