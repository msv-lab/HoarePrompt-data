#State of the program right berfore the function call: nums is a list of lists, where each sublist represents a test case and contains n+1 integers. The first integer n (1 ≤ n ≤ 2⋅10^5) is the number of containers, and the next n integers (0 ≤ a_i ≤ 10^9) are the amounts of water in the containers. The sum of a_i for each test case is divisible by n. The total number of containers across all test cases does not exceed 2⋅10^5.
def func_1(nums):
    n = len(nums)
    total = sum(nums)
    if (total % n != 0) :
        return 'NO'
        #The program returns 'NO'
    #State: `nums` is a list of lists, where each sublist represents a test case and contains n+1 integers. The first integer n (1 ≤ n ≤ 2⋅10^5) is the number of containers, and the next n integers (0 ≤ a_i ≤ 10^9) are the amounts of water in the containers. The sum of a_i for each test case is divisible by n. The total number of containers across all test cases does not exceed 2⋅10^5. `n` is the number of test cases. `total` is the sum of all elements in `nums`, and `total` is divisible by `n`.
    mean = total // n
    curr = 0
    for i in range(n):
        curr += nums[i] - mean
        
        if curr < 0:
            return 'NO'
        
    #State: Since the problem does not specify that the function returns early, and assuming the loop completes without returning 'NO', the final value of `curr` would be 0 (as the sum of all deviations from the mean across all test cases should balance out to zero).
    #
    #Output State:
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` accepts a list of lists, where each sublist represents a test case containing `n+1` integers. The first integer `n` specifies the number of containers, and the subsequent `n` integers represent the amounts of water in these containers. The function checks if it is possible to redistribute the water in the containers such that each container has the same amount, given that the total amount of water is divisible by `n`. If the redistribution condition is met, it returns 'YES'; otherwise, it returns 'NO'.

