#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    if (n >= 5) :
        return 0
        #The program returns 0
    else :
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
            
        #State of the program after the  for loop has been executed: `n` is a non-negative integer less than 5, `factorial` is the factorial of `n`
        return factorial % 10
        #The program returns the last digit of the factorial of 'n'. 'n' is a non-negative integer less than 5 and 'factorial' is the factorial of 'n'.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n`. 
If `n` is greater than or equal to 5, the function returns 0. 
If `n` is less than 5, the function calculates the factorial of `n` and returns the last digit of the factorial. 
Therefore, the functionality of the function `func_1` is to return 0 if `n` is greater than or equal to 5, and the last digit of the factorial of `n` if `n` is less than 5.

