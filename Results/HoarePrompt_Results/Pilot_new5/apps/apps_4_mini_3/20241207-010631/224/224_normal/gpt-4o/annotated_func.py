#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^6, and mod is a positive integer (typically 1000000007).
def func_1(n, mod):
    result = 1
    for i in range(2, n + 1):
        result = result * i % mod
        
    #State of the program after the  for loop has been executed: `result` is equal to the factorial of `n` modulo `mod`, `n` is an integer such that 2 <= n <= 10^6, `mod` is a positive integer.
    return result
    #The program returns the factorial of n modulo mod, where n is an integer such that 2 <= n <= 10^6 and mod is a positive integer.
#Overall this is what the function does:The function accepts an integer `n` (where 2 <= n <= 10^6) and a positive integer `mod`. It computes and returns the factorial of `n` modulo `mod`. The function does not handle cases where `n` is less than 2 or greater than 10^6, but given the constraints in the annotations, it is expected to work within these bounds.

