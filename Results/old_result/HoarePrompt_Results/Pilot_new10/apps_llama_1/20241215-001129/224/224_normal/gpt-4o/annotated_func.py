#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^6, and mod is an integer equal to 10^9 + 7.
def func_1(n, mod):
    result = 1
    for i in range(2, n + 1):
        result = result * i % mod
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= n <= 10^6, `mod` is 10^9 + 7, `result` is the factorial of `n` starting from 2 (2 * 3 *... * n) modulo `mod`, and `i` equals `n`.
    return result
    #The program returns the factorial of `n` (starting from 2) modulo 10^9 + 7, where 2 <= n <= 10^6.
#Overall this is what the function does:The function calculates the factorial of `n` starting from 2 (or returns 1 if `n` is 0 or 1) and returns this value modulo `mod`, for any integer `n` and `mod`, without explicit error checking for the constraints on `n` and `mod`.

