#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each of the t test cases, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
def func_1(n):
    if (n == 0) :
        return -1
        #The program returns -1
    #State: t is an integer such that 1 ≤ t ≤ 10^4, and for each of the t test cases, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5, and n is not equal to 0.
    position = 0
    while n != 0:
        n >>= 1
        
        position += 1
        
    #State: For each test case, `n` is 0 and `position` is the number of bits in the binary representation of the original `n`.
    return position - 1
    #The program returns 0
#Overall this is what the function does:The function `func_1` accepts an integer `n` such that 1 ≤ n ≤ 2 · 10^5. The function returns -1 if `n` is 0; otherwise, it returns the position of the most significant bit in the binary representation of `n` minus one.

