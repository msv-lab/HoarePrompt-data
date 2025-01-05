#State of the program right berfore the function call: **
def func_1(a, b):
    c = a + b
    if (c >= mod) :
        c -= mod
    #State of the program after the if block has been executed: *`a`, `b`, `c` are integers. If c >= mod, then the function executes without any changes to a, b, or c.
    return c
    #The program returns the integer value of c
#Overall this is what the function does:The function `func_1` accepts two integer parameters `a` and `b`. It calculates the sum of `a` and `b`, and if the sum is greater than or equal to the value of `mod`, it subtracts `mod` from the sum. The function then returns the resulting integer value of `c`.

#State of the program right berfore the function call: N and K are non-negative integers such that 1 <= N <= 2*10^5 and 0 <= K <= 2*10^5. H_i is an integer such that 1 <= H_i <= 10^9 for each i in the range [1, N].**
def func_2():
    H, N = [int(x) for x in raw_input().split()]
    s = sum([int(x) for x in raw_input().split()])
    if (s >= H) :
        print('Yes')
    else :
        print('No')
    #State of the program after the if-else block has been executed: *N and K are non-negative integers such that 1 <= N <= 2*10^5 and 0 <= K <= 2*10^5, H_i is an integer such that 1 <= H_i <= 10^9 for each i in the range [1, N]; H is an integer, N is an integer. s is an integer. If s is greater than or equal to H, then a certain condition is met. Otherwise, a different condition is met.
#Overall this is what the function does:The function `func_2` reads input for integers H and N, and then reads a list of integers to calculate their sum. It compares the sum to H and prints 'Yes' if the sum is greater than or equal to H, otherwise it prints 'No'. The function does not accept any parameters and does not return any specific output based on the inputs.

