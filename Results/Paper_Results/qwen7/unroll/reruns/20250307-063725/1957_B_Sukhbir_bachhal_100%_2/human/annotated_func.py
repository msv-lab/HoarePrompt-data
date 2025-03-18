#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and k are integers satisfying 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9. Additionally, the sum of all n over all test cases does not exceed 2⋅10^5.
def func_1(n):
    if (n == 0) :
        return -1
        #The program returns -1
    #State: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers satisfying 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9, and n is not equal to 0. Additionally, the sum of all n over all test cases does not exceed 2⋅10^5.
    position = 0
    while n != 0:
        n >>= 1
        
        position += 1
        
    #State: The variable `n` will be 0 and `position` will be the number of times `n` can be right-shifted until it becomes 0.
    return position - 1
    #The program returns -1
#Overall this is what the function does:The function `func_1` accepts an integer `n` within the range 1 ≤ n ≤ 2⋅10^5 and returns -1. Regardless of the value of `n`, the function always returns -1.

