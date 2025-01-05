#State of the program right berfore the function call: n is a non-negative integer.**
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *n is a non-negative integer. If n % 10 != 0, s is 1. Otherwise, s remains 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function reads an input integer n, checks if n is not divisible by 10 and sets s to 1 in that case, otherwise s remains 0. It then prints the result of the expression 2 * (n / 10) + s. The function doesn't accept any parameters and doesn't have a specified output. There is a potential issue with the division operation as the input n is taken as a string and not converted to an integer. This can lead to unexpected results or errors when trying to perform arithmetic operations.

