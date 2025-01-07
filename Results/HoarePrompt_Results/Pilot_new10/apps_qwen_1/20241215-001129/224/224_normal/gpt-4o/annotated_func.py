#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^6, and mod is the integer 1000000007.
def func_1(n, mod):
    result = 1
    for i in range(2, n + 1):
        result = result * i % mod
        
    #State of the program after the  for loop has been executed: `total` is 1, `mod` is 1000000007, `n` is an integer such that \(2 \leq n \leq 10^6\), `result` is the factorial of `n` modulo `mod`, `i` is `n` + 1
    return result
    #The program returns result, which is the factorial of n modulo mod
#Overall this is what the function does:The function `func_1` accepts two parameters: `n` (an integer such that \(2 \leq n \leq 10^6\)) and `mod` (an integer equal to 1000000007). It calculates the factorial of `n` modulo `mod` by iterating from 2 to `n` and multiplying each number by the current result modulo `mod`. The function returns the final result, which is the factorial of `n` modulo `mod`.

