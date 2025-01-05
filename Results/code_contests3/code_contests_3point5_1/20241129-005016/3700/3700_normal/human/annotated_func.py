#State of the program right berfore the function call: **
def func_1(a, b):
    c = a + b
    if (c >= mod) :
        c -= mod
    #State of the program after the if block has been executed: *`a`, `b`, `c` are integers where `c` is the sum of `a` and `b`. If `c` is greater than or equal to `mod`, the program state remains the same.
    return c
    #The program returns the sum of integers `a` and `b` which is stored in variable `c`. If `c` is greater than or equal to `mod`, the program state remains the same.
#Overall this is what the function does:The function func_1 accepts two integer parameters a and b, calculates their sum, and stores it in c. If the sum of a and b is greater than or equal to mod, it subtracts mod from the sum before returning the result.

#State of the program right berfore the function call: N and K are non-negative integers such that 1 <= N <= 2*10^5 and 0 <= K <= 2*10^5. H_i are positive integers such that 1 <= H_i <= 10^9.**
def func_2():
    H, N = [int(x) for x in raw_input().split()]
    s = sum([int(x) for x in raw_input().split()])
    if (s >= H) :
        print('Yes')
    else :
        print('No')
    #State of the program after the if-else block has been executed: *`N` and `K` are non-negative integers, `H_i` are positive integers, `s` is the sum of integers obtained from the input split. If the sum `s` is greater than or equal to `H`, the program continues normally. Otherwise, the program prints 'No'.
#Overall this is what the function does:The function `func_2` reads two non-negative integers `H` and `N`, where `H` is a positive integer and `N` is a non-negative integer. It then calculates the sum of a list of integers based on user input. If the sum is greater than or equal to `H`, it prints 'Yes'; otherwise, it prints 'No'. The function does not accept any parameters and does not return any specific value.

