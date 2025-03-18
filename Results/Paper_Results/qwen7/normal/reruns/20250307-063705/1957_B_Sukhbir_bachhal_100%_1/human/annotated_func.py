#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and k are integers satisfying 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9. The sum of all n values across test cases does not exceed 2⋅10^5.
def func_1(n):
    if (n == 0) :
        return -1
        #The program returns -1
    #State: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and k are integers satisfying 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9. The sum of all n values across test cases does not exceed 2⋅10^5. Additionally, n is not equal to 0.
    position = 0
    while n != 0:
        n >>= 1
        
        position += 1
        
    #State: Output State: The final position is 32, and n is 0.
    #
    #Explanation: The loop continues to right-shift `n` by 1 bit and increment `position` until `n` becomes 0. Since each iteration halves the value of `n` (in terms of its binary representation), it takes 32 iterations for a 32-bit integer starting from `2^32 - 1` (or any non-zero value) to become 0. After 32 iterations, `position` will be 32, and `n` will be 0.
    return position - 1
    #The program returns 31
#Overall this is what the function does:The function `func_1` accepts an integer `n` within the range 1 ≤ n ≤ 2⋅10^5. It performs a series of right shifts on `n` until it becomes zero, counting the number of shifts. If `n` is zero initially, the function returns -1. Otherwise, it returns 31, indicating that it took 32 iterations to reduce `n` to zero, which is the maximum number of bits in a 32-bit integer.

