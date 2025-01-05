#State of the program right berfore the function call: **
def func_1(a, b):
    c = a + b
    if (c >= mod) :
        c -= mod
    #State of the program after the if block has been executed: *`a`, `b`, `c` are integers. If `c` is the sum of `a` and `b`, and `c` is greater than or equal to `mod`, then the program executes the if block. Otherwise, there is no change in the values of `a`, `b`, and `c`.
    return c
    #The program returns the value of 'c' which is the sum of 'a' and 'b', only if 'c' is greater than or equal to 'mod'
#Overall this is what the function does:The function func_1 accepts two integer parameters a and b, calculates their sum, and returns the sum only if it is greater than or equal to the value of mod. If the sum of a and b is greater than or equal to mod, it subtracts mod from the sum and returns the result. If the sum of a and b is less than mod, the function does not modify the sum and returns it as is.

#State of the program right berfore the function call: N and K are integers such that 1 <= N <= 2 * 10^5 and 0 <= K <= 2 * 10^5. H_i are integers such that 1 <= H_i <= 10^9.**
def func_2():
    H, N = [int(x) for x in raw_input().split()]
    s = sum([int(x) for x in raw_input().split()])
    if (s >= H) :
        print('Yes')
    else :
        print('No')
    #State of the program after the if-else block has been executed: *`N` and `K` are integers such that 1 <= N <= 2 * 10^5, 0 <= K <= 2 * 10^5, `H_i` are integers such that 1 <= H_i <= 10^9, `H` and `N` are assigned values from the input after converting them to integers; `s` is the sum of integers obtained from the input. If the sum `s` is greater than or equal to `H`, then the program executes the if part. If the sum `s` is less than `H`, then the program executes the else part.
#Overall this is what the function does:The function `func_2` reads two integers `H` and `N` from the input, calculates the sum `s` of integers also provided in the input, and then prints 'Yes' if `s` is greater than or equal to `H`, otherwise it prints 'No'. The function does not accept any parameters and does not return any specific value.

