#State of the program right berfore the function call: **
def func_1(a, b):
    c = a + b
    if (c >= mod) :
        c -= mod
    #State of the program after the if block has been executed: *`c` is the result of `a + b`. If `c` is greater than or equal to `mod`, then the program has the value of `c`.
    return c
    #The program returns the value of variable `c` if it is greater than or equal to the value of `mod`
#Overall this is what the function does:The function `func_1` accepts two parameters `a` and `b`, calculates the sum `c = a + b`, and then checks if `c` is greater than or equal to the value of `mod`. If `c` meets this condition, the function returns `c`. If `c` is not greater than or equal to `mod`, the function does not return anything.

#State of the program right berfore the function call: **
def func_2():
    H, N = [int(x) for x in raw_input().split()]
    s = sum([int(x) for x in raw_input().split()])
    if (s >= H) :
        print('Yes')
    else :
        print('No')
    #State of the program after the if-else block has been executed: *`H`, `N`, `s` are values based on input. If the sum of integers entered by the user is greater than or equal to `H`, the function does something. Otherwise, there is no else part in the code.
#Overall this is what the function does:The function func_2 reads two integers `H` and `N` from user input and calculates the sum `s` of `N` integers entered by the user. If the sum `s` is greater than or equal to `H`, it prints 'Yes'; otherwise, it prints 'No'. The function does not accept any parameters and returns a predefined string output based on the comparison of `s` and `H`.

