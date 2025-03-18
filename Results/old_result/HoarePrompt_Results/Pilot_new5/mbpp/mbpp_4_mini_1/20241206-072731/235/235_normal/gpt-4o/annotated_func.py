#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    total = 0
    while n > 0:
        total += n % 10
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is 0, `total` is the sum of the digits of the original value of `n`. If the original value of `n` was 0, then `total` remains 0.
    return total
    #The program returns the total, which is the sum of the digits of the original value of n, and since n is 0, total remains 0.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns the sum of its digits. If `n` is 0, it returns 0. If `n` is any non-negative integer, it calculates the sum by iterating through each digit of `n`.

