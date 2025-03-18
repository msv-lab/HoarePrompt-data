#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    total = 0
    while n > 0:
        total += n % 10
        
        n //= 10
        
    #State of the program after the loop has been executed: 'n' is 0, 'total' is the sum of all digits of the original value of 'n' (if original 'n' was greater than 0); if 'n' was 0 initially, 'total' remains 0.
    return total
    #The program returns total, which is 0 since 'n' is 0 and no digits were summed.
#Overall this is what the function does:The function accepts a non-negative integer `n`, calculates the sum of its digits, and returns this sum. If `n` is 0, the function returns 0, as there are no digits to sum.

