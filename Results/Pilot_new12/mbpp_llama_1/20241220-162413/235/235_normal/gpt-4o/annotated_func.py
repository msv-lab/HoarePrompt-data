#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    total = 0
    while n > 0:
        total += n % 10
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is 0, `total` is the sum of all the digits of the original value of `n`
    return total
    #The program returns 0
#Overall this is what the function does:The function accepts a non-negative integer parameter `n` and returns the sum of all the digits of the original value of `n`. This includes handling edge cases where `n` is 0, in which case the function returns 0, as there are no digits to sum. The function effectively calculates and returns a single numerical value that represents the sum of all digits in the input number `n`, regardless of the initial value of `n`.

