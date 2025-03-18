#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and k are integers satisfying 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9. The sum of all n values across all test cases does not exceed 2⋅10^5.
def func_1(n):
    if (n == 0) :
        return -1
        #The program returns -1
    #State: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers satisfying 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9, and n is not equal to 0. The sum of all n values across all test cases does not exceed 2⋅10^5.
    position = 0
    while n != 0:
        n >>= 1
        
        position += 1
        
    #State: Output State: `position` is 32, `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is now 0.
    #
    #Explanation: The loop continues to right-shift `n` by 1 bit and increment `position` until `n` becomes 0. Since each iteration halves the value of `n`, and it takes 32 iterations to reduce any non-zero integer within the given constraints to 0 through right-shifting, `position` will be 32 when the loop terminates. At this point, `n` will be 0 because it has been fully right-shifted. The value of `t` remains unchanged as it is not affected by the loop.
    return position - 1
    #The program returns 31
#Overall this is what the function does:The function accepts an integer `n` as input, where `1 ≤ n ≤ 2⋅10^5`. If `n` is 0, the function returns -1. Otherwise, it performs a series of right shifts on `n` until it becomes 0, counting the number of shifts. The function then returns the count minus one, which will be 31.

