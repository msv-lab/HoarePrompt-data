#State of the program right berfore the function call: **
def func_1(a, b):
    c = a + b
    if (c >= mod) :
        c -= mod
    #State of the program after the if block has been executed: *`a`, `b`, `c` are integers. If `c` is greater than or equal to `mod`, then `c` is updated by subtracting `mod` from its previous value.
    return c
    #The program returns the updated value of 'c' after checking if it is greater than or equal to 'mod' and subtracting 'mod' if necessary
#Overall this is what the function does:The function func_1 accepts two integer parameters `a` and `b`, calculates the sum of `a` and `b`, and then updates `c` by subtracting `mod` if the sum is greater than or equal to `mod`. The function returns the updated value of `c`. If `c` is less than `mod`, the function does not perform any subtraction.

#State of the program right berfore the function call: **
def func_2():
    H, N = [int(x) for x in raw_input().split()]
    s = sum([int(x) for x in raw_input().split()])
    if (s >= H) :
        print('Yes')
    else :
        print('No')
    #State of the program after the if-else block has been executed: *`H` is an integer, `N` is an integer, `s` is the sum of integers obtained from user input. If the sum of integers `s` is greater than or equal to `H`, the program prints 'Yes'. If the sum of integers `s` is less than `H`, the program prints 'No' and does not affect the initial state variables.
#Overall this is what the function does:The function func_2 reads two integers H and N from user input. It then calculates the sum of N integers provided by the user. If the sum s is greater than or equal to H, it prints 'Yes', otherwise it prints 'No'. The function does not accept any parameters and does not return any value.

