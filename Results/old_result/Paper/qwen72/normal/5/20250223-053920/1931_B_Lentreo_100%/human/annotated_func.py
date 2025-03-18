#State of the program right berfore the function call: nums is a list of integers representing the amounts of water in the containers, where the length of nums (n) is a positive integer (1 ≤ n ≤ 2 · 10^5), and each element a_i in nums is a non-negative integer (0 ≤ a_i ≤ 10^9). The sum of all elements in nums is divisible by n.
def func_1(nums):
    n = len(nums)
    total = sum(nums)
    if (total % n != 0) :
        return 'NO'
        #The program returns 'NO'
    #State: `nums` is a list of integers representing the amounts of water in the containers, where the length of `nums` (n) is a positive integer (1 ≤ n ≤ 2 · 10^5), and each element `a_i` in `nums` is a non-negative integer (0 ≤ a_i ≤ 10^9). The sum of all elements in `nums` is divisible by `n`. `n` is the length of `nums`. `total` is the sum of all elements in `nums`. `total % n` is equal to 0.
    mean = total // n
    curr = 0
    for i in range(n):
        curr += nums[i] - mean
        
        if curr < 0:
            return 'NO'
        
    #State: `curr` is 0.
    return 'YES'
    #The program returns 'YES'.
#Overall this is what the function does:The function `func_1` accepts a list of integers `nums` representing the amounts of water in containers. It checks if it is possible to redistribute the water so that all containers have the same amount of water. If the total amount of water is not divisible by the number of containers or if during the redistribution process any container would need more water than is available to reach the average, the function returns 'NO'. Otherwise, it returns 'YES'.

