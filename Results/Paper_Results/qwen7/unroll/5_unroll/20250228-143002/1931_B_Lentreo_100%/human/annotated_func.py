#State of the program right berfore the function call: nums is a list of integers representing the amounts of water in each container, where the length of nums is n (1 ≤ n ≤ 2 \cdot 10^5) and the sum of the integers in nums is divisible by n (1 ≤ n ≤ 2 \cdot 10^9).
def func_1(nums):
    n = len(nums)
    total = sum(nums)
    if (total % n != 0) :
        return 'NO'
        #The program returns 'NO'
    #State: `nums` is a list of integers representing the amounts of water in each container, `n` is the length of `nums`, `total` is the sum of all elements in `nums`. The total sum of `nums` is divisible by `n`.
    mean = total // n
    curr = 0
    for i in range(n):
        curr += nums[i] - mean
        
        if curr < 0:
            return 'NO'
        
    #State: Output State: curr is -n, nums is a list of integers representing the amounts of water in each container, n is the length of nums, total is the sum of all elements in nums, and mean is the integer division of total by n.
    #
    #Explanation: After iterating through all elements in `nums`, `curr` accumulates the difference between each element and the mean. If at any point `curr` becomes less than 0, the function returns 'NO'. If the loop completes without returning, `curr` will be the sum of all differences from the mean, which is equivalent to `-n` because each element in `nums` contributes to making `curr` less than 0 exactly once before the loop ends.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function accepts a list of integers `nums` and checks if it's possible to partition `nums` into `n` (where `n` is the length of `nums`) non-empty parts such that the sum of each part is equal. If such a partition exists, it returns 'YES'; otherwise, it returns 'NO'.

