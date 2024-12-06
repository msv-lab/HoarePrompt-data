#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^6, and mod is a positive integer.
def func_1(n, mod):
    result = 1
    for i in range(2, n + 1):
        result = result * i % mod
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= `n` <= 10^6, `result` is equal to the product of integers from 2 to `n` modulo `mod`.
    return result
    #The program returns the product of integers from 2 to n modulo mod, where n is an integer such that 2 <= n <= 10^6.
#Overall this is what the function does:The function accepts an integer `n` (where 2 <= n <= 10^6) and a positive integer `mod`, and returns the product of all integers from 2 to `n`, calculated modulo `mod`. There are no checks for invalid inputs; thus, it assumes that `n` and `mod` are valid according to the specified constraints.

