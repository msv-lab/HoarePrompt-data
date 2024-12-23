#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    total = 0
    while n > 0:
        total += n % 10
        
        n //= 10
        
    #State of the program after the loop has been executed: 'total' is the sum of all digits of the original value of 'n', 'n' is 0
    return total
    #The program returns 0, as 'total' is the sum of all digits of the original value of 'n', and 'n' is 0
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and calculates the sum of its digits. After the loop, `n` becomes 0, and `total` contains the sum of the digits of the original `n`. The function then returns the value of `total`, which is the sum of the digits of the original `n`.

