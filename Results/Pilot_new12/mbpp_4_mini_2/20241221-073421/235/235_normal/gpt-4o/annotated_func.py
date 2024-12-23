#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    total = 0
    while n > 0:
        total += n % 10
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is 0, `total` is the sum of the digits of the original value of `n`, if the original `n` was greater than 0; if the original `n` was 0, then `total` remains 0.
    return total
    #The program returns total, which remains 0 since the original value of n was 0.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns the sum of its digits. If `n` is 0, the function returns 0. The function effectively processes all non-negative integers, breaking them down digit by digit to accumulate their sum, irrespective of their length. Thus, for any valid input `n`, the output will always be a non-negative integer corresponding to the sum of the individual digits of `n`.

