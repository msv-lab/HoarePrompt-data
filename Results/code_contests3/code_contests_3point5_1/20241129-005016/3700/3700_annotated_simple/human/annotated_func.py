#State of the program right berfore the function call: **
def func_1(a, b):
    c = a + b
    if (c >= mod) :
        c -= mod
    #State of the program after the if block has been executed: *`a`, `b`, `c` are integers. If `c` is greater than or equal to `mod`, then `c` is updated to its remainder when divided by `mod`. If `c` is less than `mod`, no changes are made to `c`.
    return c
    #The program returns the value of 'c' after checking if it is greater than or equal to 'mod', and updating 'c' to its remainder when divided by 'mod' if necessary. If 'c' is less than 'mod', 'c' remains unchanged
#Overall this is what the function does:The function func_1 accepts two integer parameters a and b, calculates c = a + b, and returns the value of c. If c is greater than or equal to mod, it updates c to its remainder when divided by mod. If c is less than mod, c remains unchanged. The function does not handle cases where mod is not defined or is 0.

#State of the program right berfore the function call: N and K are non-negative integers such that 1 <= N <= 2 * 10^5 and 0 <= K <= 2 * 10^5. H_i are positive integers such that 1 <= H_i <= 10^9.**
def func_2():
    H, N = [int(x) for x in raw_input().split()]
    s = sum([int(x) for x in raw_input().split()])
    if (s >= H) :
        print('Yes')
    else :
        print('No')
    #State of the program after the if-else block has been executed: *`N` and `K` are non-negative integers such that 1 <= N <= 2 * 10^5 and 0 <= K <= 2 * 10^5. `H_i` are positive integers such that 1 <= H_i <= 10^9; `H` and `N` are assigned values from the input split by space. `s` is the sum of integers obtained from the input split by space. If the sum `s` is greater than or equal to `H`, 'Yes' is printed. If the sum `s` is less than `H`, no output is generated.
#Overall this is what the function does:The function `func_2` reads two integers `H` and `N` from the input, then calculates the sum `s` of integers also read from the input. If the sum `s` is greater than or equal to `H`, it prints 'Yes'; otherwise, it prints 'No'. The function does not accept any parameters explicitly, and it handles the mentioned constraints accurately.

