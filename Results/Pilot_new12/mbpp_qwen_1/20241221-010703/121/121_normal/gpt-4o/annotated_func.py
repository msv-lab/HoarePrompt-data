#State of the program right berfore the function call: n is a positive integer.
def func_1(n):
    if (n == 0 or n == 1) :
        return 1
        #The program returns 1
    #State of the program after the if block has been executed: `n` is a positive integer and `n` is neither 0 nor 1
    S0, S1 = 1, 1
    for i in range(2, n + 1):
        S_next = 2 * S1 + S0
        
        S0, S1 = S1, S_next
        
    #State of the program after the  for loop has been executed: `n` is a positive integer and neither 0 nor 1; `S0` is 1; `S1` is 1; `i` is `n`; `S0` is \((-2^n - 1) / (-7)\) * `S0`; `S1` is \((-2^n + 1) / (-7)\) * `S0`
    return S1
    #The program returns \(\frac{-2^n + 1}{-7} \times \frac{-2^n - 1}{-7}\) where \(n\) is a positive integer and neither 0 nor 1
#Overall this is what the function does:The function `func_1` accepts a parameter `n`, which is a positive integer. It returns 1 if `n` is either 0 or 1. For any other positive integer value of `n`, it calculates and returns the value of \(\frac{-2^n + 1}{-7} \times \frac{-2^n - 1}{-7}\).

