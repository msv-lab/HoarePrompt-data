#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    total = 0
    while n > 0:
        total += n % 10
        
        n //= 10
        
    #State of the program after the loop has been executed: 'n' is 0, 'total' is the sum of all digits of the original value of 'n'
    return total
    #The program returns total which is the sum of all digits of the original value of n (which is 0)
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and returns the sum of all its digits. The function iterates through each digit of `n`, adding them to a cumulative total. After processing all digits, `n` is reduced to 0. The final state of the program is that the function returns the total sum of the digits of the original value of `n`.

