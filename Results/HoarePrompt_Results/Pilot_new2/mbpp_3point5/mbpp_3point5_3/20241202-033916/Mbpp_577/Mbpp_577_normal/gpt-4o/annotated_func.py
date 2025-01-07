#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    if (n >= 5) :
        return 0
        #The program returns 0 if the current value of n is greater than or equal to 5
    else :
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
            
        #State of the program after the  for loop has been executed: n is greater than or equal to 4, factorial is equal to 24, i is equal to 4
        return factorial % 10
        #The program returns 4, as the remainder of 24 divided by 10 is 4
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and has two cases:
- Case 1: If the current value of `n` is greater than or equal to 5, the function returns 0.
- Case 2: If the current value of `n` is less than 5, the function calculates the factorial of `n` and returns the last digit of the factorial. 
Therefore, the functionality of the function is to return 0 if `n` is greater than or equal to 5, and return the last digit of the factorial if `n` is less than 5.

