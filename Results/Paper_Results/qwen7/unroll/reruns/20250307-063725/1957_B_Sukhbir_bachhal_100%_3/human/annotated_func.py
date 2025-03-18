#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and k are integers satisfying 1 ≤ n ≤ 2·10^5 and 1 ≤ k ≤ 10^9. Additionally, the sum of all n over all test cases does not exceed 2·10^5.
def func_1(n):
    if (n == 0) :
        return -1
        #The program returns -1
    #State: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers satisfying 1 ≤ n ≤ 2·10^5 and 1 ≤ k ≤ 10^9, and n is not equal to 0. Additionally, the sum of all n over all test cases does not exceed 2·10^5.
    position = 0
    while n != 0:
        n >>= 1
        
        position += 1
        
    #State: The value of `position` will be the number of bits (1s) in the binary representation of `n`, and `n` will be 0.
    return position - 1
    #The program returns -1
#Overall this is what the function does:The function `func_1` accepts an integer `n` as input. If `n` is 0, it returns -1. Otherwise, it calculates the number of bits (1s) in the binary representation of `n` and returns this count minus one. In both cases, the function ultimately returns -1.

