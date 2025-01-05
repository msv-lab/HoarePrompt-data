#State of the program right berfore the function call: **
def func_1(a, b):
    c = a + b
    if (c >= mod) :
        c -= mod
    #State of the program after the if block has been executed: *`a`, `b`, `c`, `mod` are integers. If `c` is greater than or equal to the value of `mod` after subtracting `mod`, then the function updates `c` to be the remainder when divided by `mod`. Otherwise, there is no change in the values of `a`, `b`, and `c`.
    return c
    #The program returns the updated value of 'c' after the condition check and possibly updating it to be the remainder when divided by 'mod'.
#Overall this is what the function does:The function `func_1` accepts two integer parameters `a` and `b`. It calculates the sum of `a` and `b` and stores the result in `c`. If the value of `c` is greater than or equal to the integer `mod`, it updates `c` to be the remainder when divided by `mod`. The function then returns the updated value of `c`. The functionality of the function is to perform this arithmetic operation and return the final value of `c`, possibly adjusted to be the remainder when divided by `mod`.

#State of the program right berfore the function call: N and K are integers such that 1 <= N <= 2 * 10^5, 0 <= K <= 2 * 10^5. H_i are integers such that 1 <= H_i <= 10^9.**
def func_2():
    H, N = [int(x) for x in raw_input().split()]
    s = sum([int(x) for x in raw_input().split()])
    if (s >= H) :
        print('Yes')
    else :
        print('No')
    #State of the program after the if-else block has been executed: *`N`, `K`, `H_i` are integers, `s` is the sum of integers parsed from input. If the sum `s` is greater than or equal to `H`, the program prints 'Yes'. Otherwise, if the sum `s` is less than `H`, the program prints 'No'.
#Overall this is what the function does:The function `func_2` reads two integers `H` and `N` from the input, calculates the sum `s` of `N` integers also read from the input, and then prints 'Yes' if the sum `s` is greater than or equal to `H`, otherwise it prints 'No'. The function does not accept any parameters and does not return any specific value. However, the code does not handle any exceptions or edge cases like invalid inputs or out-of-range values.

