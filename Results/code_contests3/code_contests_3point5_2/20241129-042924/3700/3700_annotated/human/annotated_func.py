#State of the program right berfore the function call: **
def func_1(a, b):
    c = a + b
    if (c >= mod) :
        c -= mod
    #State of the program after the if block has been executed: *`c` is the sum of `a` and `b`. If `c` is greater than or equal to `mod`, no changes are made to the variables.
    return c
    #The program returns the sum of variables `a` and `b`, unless the sum is greater than or equal to `mod`, in which case no changes are made to the variables.
#Overall this is what the function does:The function func_1 accepts two integer parameters `a` and `b`, calculates their sum and returns it. If the sum is greater than or equal to `mod`, the function subtracts `mod` from the sum before returning. If the sum is less than `mod`, it returns the sum without modification.

#State of the program right berfore the function call: N and K are non-negative integers such that 1 <= N <= 2*10^5 and 0 <= K <= 2*10^5. H_i are positive integers such that 1 <= H_i <= 10^9.**
def func_2():
    H, N = [int(x) for x in raw_input().split()]
    s = sum([int(x) for x in raw_input().split()])
    if (s >= H) :
        print('Yes')
    else :
        print('No')
    #State of the program after the if-else block has been executed: *N and K are non-negative integers such that 1 <= N <= 2*10^5 and 0 <= K <= 2*10^5; H_i are positive integers such that 1 <= H_i <= 10^9; H, N are assigned values based on the input split; s is the sum of integers entered. If the sum of integers entered is greater than or equal to H, the program prints 'Yes'. If the sum of integers entered is less than H, the program prints 'No'.
#Overall this is what the function does:The function `func_2` reads input integers H and N, then calculates the sum of N integers. If the sum is greater than or equal to H, it prints 'Yes'; otherwise, it prints 'No'. The function does not accept any parameters and does not return any value.

