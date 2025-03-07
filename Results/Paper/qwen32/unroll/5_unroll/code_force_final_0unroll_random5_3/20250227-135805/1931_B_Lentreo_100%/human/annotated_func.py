#State of the program right berfore the function call: nums is a list of lists, where each inner list represents a test case. Each test case starts with an integer n (1 ≤ n ≤ 2 · 10^5) indicating the number of containers, followed by n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ 10^9) representing the amounts of water in the containers. It is guaranteed that the sum of a_i in each test case is divisible by n and does not exceed 2 · 10^9. The total number of containers across all test cases does not exceed 2 · 10^5.
def func_1(nums):
    n = len(nums)
    total = sum(nums)
    if (total % n != 0) :
        return 'NO'
        #The program returns 'NO'
    #State: `nums` is a list of lists, where each inner list represents a test case. Each test case starts with an integer n (1 ≤ n ≤ 2 · 10^5) indicating the number of containers, followed by n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ 10^9) representing the amounts of water in the containers. It is guaranteed that the sum of a_i in each test case is divisible by n and does not exceed 2 · 10^9. The total number of containers across all test cases does not exceed 2 · 10^5. `n` is the number of test cases in `nums`. `total` is the sum of all integers within all inner lists of `nums`. Additionally, `total` is perfectly divisible by `n`.
    mean = total // n
    curr = 0
    for i in range(n):
        curr += nums[i] - mean
        
        if curr < 0:
            return 'NO'
        
    #State: `nums` is a list of lists, where each inner list represents a test case. `total` is the sum of all integers within all inner lists of `nums`. `mean` is the integer value of `total` divided by `n`. `curr` is 0.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` evaluates a list of test cases, where each test case consists of a number of containers and their respective water amounts. It checks if it's possible to redistribute the water in each test case such that all containers have the same amount of water. If it is possible, the function returns 'YES'; otherwise, it returns 'NO'.

