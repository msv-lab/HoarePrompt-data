#State of the program right berfore the function call: nums is a list of lists, where each inner list represents a test case and contains n+1 integers. The first integer n (1 ≤ n ≤ 2 · 10^5) is the number of containers, and the following n integers (0 ≤ a_i ≤ 10^9) are the amounts of water in the containers. The sum of a_i in each test case is divisible by n. The total number of test cases t (1 ≤ t ≤ 10^4) is given in the first line of the input, and the sum of n over all test cases does not exceed 2 · 10^5.
def func_1(nums):
    n = len(nums)
    total = sum(nums)
    if (total % n != 0) :
        return 'NO'
        #The program returns 'NO'
    #State: `nums` is a list of lists where each inner list represents a test case and contains n+1 integers; `n` is the number of test cases (equal to the length of `nums`); `total` is the sum of all integers in all inner lists of `nums`. Additionally, `total` is divisible by `n`
    mean = total // n
    curr = 0
    for i in range(n):
        curr += nums[i] - mean
        
        if curr < 0:
            return 'NO'
        
    #State: `curr` is the sum of `nums[i] - mean` for all `i` from `0` to `n-1`, and the function does not return 'NO'.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` evaluates a list of test cases where each test case consists of a number of containers and their respective water amounts. It checks if it's possible to redistribute the water in such a way that all containers in each test case end up with the same amount of water, given that the total amount of water is divisible by the number of containers. If the redistribution is possible, it returns 'YES'; otherwise, it returns 'NO'.

