#State of the program right berfore the function call: The function `func_1` takes a single integer `t` (1 ≤ t ≤ 10^4) as input, representing the number of test cases. For each test case, it receives two integers `n` (1 ≤ n ≤ 2 · 10^5) and `k` (1 ≤ k ≤ 10^9), where `n` is the number of non-negative integers to be constructed and `k` is their sum. The sum of `n` over all test cases does not exceed 2 · 10^5.
def func_1(n):
    if (n == 0) :
        return -1
        #The program returns -1
    #State: The function `func_1` takes a single integer `t` (1 ≤ t ≤ 10^4) as input, representing the number of test cases. For each test case, it receives two integers `n` (1 ≤ n ≤ 2 · 10^5) and `k` (1 ≤ k ≤ 10^9), where `n` is the number of non-negative integers to be constructed and `k` is their sum. The sum of `n` over all test cases does not exceed 2 · 10^5. Additionally, `n` is not equal to 0.
    position = 0
    while n != 0:
        n >>= 1
        
        position += 1
        
    #State: n = 0, position = number of bits in the binary representation of the initial n
    return position - 1
    #The program returns 0
#Overall this is what the function does:The function `func_1` accepts a single integer `n`. If `n` is 0, it returns -1. Otherwise, it calculates the number of bits in the binary representation of `n` and returns this value minus 1.

