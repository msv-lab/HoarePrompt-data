#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and k are integers satisfying 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9. The sum of all n values across all test cases does not exceed 2⋅10^5.
def func_1(n):
    if (n == 0) :
        return -1
        #The program returns -1
    #State: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and k are integers satisfying 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9. The sum of all n values across all test cases does not exceed 2⋅10^5. Additionally, n is not equal to 0
    position = 0
    while n != 0:
        n >>= 1
        
        position += 1
        
    #State: position is 16 and n is 0.
    return position - 1
    #The program returns 15
#Overall this is what the function does:The function accepts an integer `n` within the range of 1 to 10^4. It checks if `n` is zero; if so, it returns -1. Otherwise, it repeatedly divides `n` by 2 until `n` becomes zero, counting the number of divisions. Finally, it returns the count minus one, which will be 15 in this case.

