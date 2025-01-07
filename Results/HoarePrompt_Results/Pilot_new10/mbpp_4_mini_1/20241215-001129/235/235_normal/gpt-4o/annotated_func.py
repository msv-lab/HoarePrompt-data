#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    total = 0
    while n > 0:
        total += n % 10
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is 0, `total` is the sum of all digits of the original value of `n`. If the original `n` was non-negative (including 0), the loop will execute only if `n` was greater than 0 to contribute to `total`. If `n` was initially 0, `total` remains 0.
    return total
    #The program returns total which is the sum of all digits of the original value of n, and since n is 0, total remains 0.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns the sum of its digits. If `n` is 0, the function returns 0, and if `n` is positive, it calculates the sum of all its digits by repeatedly extracting the last digit of `n` until `n` becomes 0. There are no error conditions or exceptions handled in the function.

