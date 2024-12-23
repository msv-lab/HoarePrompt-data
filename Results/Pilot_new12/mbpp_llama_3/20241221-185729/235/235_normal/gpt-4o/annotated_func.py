#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    total = 0
    while n > 0:
        total += n % 10
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is 0, `total` is the sum of all digits of the original value of `n`
    return total
    #The program returns total which is the sum of all digits of the original value of `n` and is equal to 0
#Overall this is what the function does:The function accepts a non-negative integer `n` as input and returns the sum of all its digits. The return value can be any non-negative integer, not necessarily 0, as the annotated code and return postconditions suggest. The function handles all non-negative integers, including 0, and correctly calculates the sum of their digits. After execution, the function's state is concluded, and it returns the calculated sum, which is the total of all digits of the original input value `n`. The function does not modify the input variable `n` outside of its local scope. It only returns the calculated sum.

