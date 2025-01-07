#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    total = 0
    while n > 0:
        total += n % 10
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is 0, `total` is the sum of all digits of the original value of `n`
    return total
    #The program returns the sum of all digits of the original value of n, which is 0, so total is also 0.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns the sum of its digits. If `n` is 0, the function returns 0. The function correctly handles all non-negative integers by iterating through each digit, summing them until `n` is reduced to 0.

