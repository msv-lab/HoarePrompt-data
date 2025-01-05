#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9.**
def func():
    n = int(raw_input())
    if (n <= 2) :
        print - 1
    else :
        if (n & 1) :
            print(n * n - 1) / 2, (n * n + 1) / 2
        else :
            print(n * n / 4 - 1), n * n / 4 + 1
        #State of the program after the if-else block has been executed: *n is a positive integer larger than 2. If n is a positive odd integer larger than 2, (n * n - 1) / 2 and (n * n + 1) / 2 are calculated and printed. If n is a positive integer larger than 2 and it is even, no calculations are performed.
    #State of the program after the if-else block has been executed: *n is a positive integer. If n <= 2, -1 is returned. If n is a positive odd integer larger than 2, (n * n - 1) / 2 and (n * n + 1) / 2 are calculated and printed. If n is a positive integer larger than 2 and it is even, no calculations are performed.
#Overall this is what the function does:The function `func` reads an integer `n` as input and performs calculations based on the value of `n`. If `n` is less than or equal to 2, it prints -1. If `n` is a positive odd integer larger than 2, it calculates and prints ((n * n - 1) / 2) and ((n * n + 1) / 2). If `n` is a positive even integer larger than 2, it calculates and prints (n * n / 4 - 1) and (n * n / 4 + 1). The function does not return any value.

