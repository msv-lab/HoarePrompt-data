#State of the program right berfore the function call: nums is a list of lists where each inner list contains n integers (1 ≤ n ≤ 2 \cdot 10^5) representing the amounts of water in the containers for each test case. The sum of the integers in each inner list is divisible by n. The length of nums (t) is between 1 and 10^4, and the sum of n over all test cases does not exceed 2 \cdot 10^5. Each integer a_i in the inner lists satisfies 0 ≤ a_i ≤ 10^9.
def func_1(nums):
    n = len(nums)
    total = sum(nums)
    if (total % n != 0) :
        return 'NO'
        #The program returns 'NO'
    #State: `nums` is a list of lists where each inner list contains `n` integers (1 ≤ `n` ≤ 2 · 10^5) representing the amounts of water in the containers for each test case. The sum of the integers in each inner list is divisible by `n`. The length of `nums` (t) is between 1 and 10^4, and the sum of `n` over all test cases does not exceed 2 · 10^5. Each integer `a_i` in the inner lists satisfies 0 ≤ `a_i` ≤ 10^9. `n` is the length of `nums`. `total` is the sum of all integers in `nums` and `total` is divisible by `n`.
    mean = total // n
    curr = 0
    for i in range(n):
        curr += nums[i] - mean
        
        if curr < 0:
            return 'NO'
        
    #State: curr is 0.
    return 'YES'
    #The program returns the string 'YES'
#Overall this is what the function does:The function `func_1` accepts a list of lists `nums`, where each inner list contains integers representing the amounts of water in containers for different test cases. It checks if it is possible to redistribute the water in each test case such that all containers have the same amount of water. If redistribution is possible for all test cases, it returns 'YES'; otherwise, it returns 'NO'.

