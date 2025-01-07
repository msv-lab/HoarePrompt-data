#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    total = 0
    while n > 0:
        total += n % 10
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is 0, `total` is the sum of the digits of the original value of `n_original`.
    return total
    #The program returns total which is the sum of the digits of the original value of n that is 0
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns the sum of its digits.

