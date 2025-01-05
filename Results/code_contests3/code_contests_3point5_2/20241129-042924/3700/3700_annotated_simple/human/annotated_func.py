#State of the program right berfore the function call: **
def func_1(a, b):
    c = a + b
    if (c >= mod) :
        c -= mod
    #State of the program after the if block has been executed: *`a`, `b`, `c` are integers. `c` is calculated as the sum of `a` and `b`. If `c` is greater than or equal to `mod`, then after the execution of the if else block, the new value of `c` is `c - mod`.
    return c
    #The program returns the value of 'c' after potentially subtracting 'mod' if 'c' is greater than or equal to 'mod'
#Overall this is what the function does:The function func_1 accepts two integer parameters `a` and `b`, calculates the sum of `a` and `b` as `c`, and returns the value of `c`. If the sum of `a` and `b` is greater than or equal to `mod`, the function subtracts `mod` from `c` before returning it.

#State of the program right berfore the function call: N and K are non-negative integers such that 1 <= N <= 2*10^5 and 0 <= K <= 2*10^5. H_i is a positive integer such that 1 <= H_i <= 10^9 for all i.**
def func_2():
    H, N = [int(x) for x in raw_input().split()]
    s = sum([int(x) for x in raw_input().split()])
    if (s >= H) :
        print('Yes')
    else :
        print('No')
    #State of the program after the if-else block has been executed: *N and K are non-negative integers such that 1 <= N <= 2*10^5 and 0 <= K <= 2*10^5. H_i is a positive integer such that 1 <= H_i <= 10^9 for all i; s is the sum of the integers obtained from the input split operation. If the sum s is greater than or equal to H, the program executes normally. Otherwise, it prints 'No'.
#Overall this is what the function does:The function `func_2` reads two integers `H` and `N` from user input, calculates the sum `s` of integers obtained from another user input, and then prints 'Yes' if `s` is greater than or equal to `H`, otherwise prints 'No'. The function does not accept any parameters and does not have a return value specified. The function operates based on the input values without any validation or error handling.

