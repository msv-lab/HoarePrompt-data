#State of the program right berfore the function call: nums is a list of lists, where each inner list represents a test case consisting of two parts: the first part is a list containing a single integer n (1 ≤ n ≤ 2 · 10^5) representing the number of containers, and the second part is a list of n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ 10^9) representing the amounts of water in the containers. The sum of a_i in each test case is guaranteed to be divisible by n. The total number of containers across all test cases does not exceed 2 · 10^5.
def func_1(nums):
    n = len(nums)
    total = sum(nums)
    if (total % n != 0) :
        return 'NO'
        #The program returns 'NO'
    #State: `nums` is a list of lists, where each inner list represents a test case consisting of two parts: the first part is a list containing a single integer n (1 ≤ n ≤ 2 · 10^5) representing the number of containers, and the second part is a list of n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ 10^9) representing the amounts of water in the containers. The sum of a_i in each test case is guaranteed to be divisible by n. The total number of containers across all test cases does not exceed 2 · 10^5. `n` is the number of test cases in `nums`. `total` is the sum of all the amounts of water across all test cases. Additionally, `total` is divisible by `n`.
    mean = total // n
    curr = 0
    for i in range(n):
        curr += nums[i] - mean
        
        if curr < 0:
            return 'NO'
        
    #State: `curr` is the sum of `(nums[i] - mean)` for all `i` from 0 to `n-1`, and `i` is `n-1`. If `curr` is less than 0 at any point during the loop, the function returns 'NO'. Otherwise, the loop completes without returning anything.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` determines whether it is possible to redistribute the water in each test case such that all containers have the same amount of water. It accepts a parameter `nums`, which is a list of lists, where each inner list represents a test case with a specified number of containers and their respective water amounts. If the water can be evenly distributed in all test cases, the function returns 'YES'; otherwise, it returns 'NO'.

