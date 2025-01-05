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
        #State of the program after the if-else block has been executed: *n is a positive odd integer larger than 2. If n is odd, the calculated values are ((n^2 - 1) / 2) and ((n^2 + 1) / 2). If n is odd and not larger than 10^9, the values printed are (((n^2) / 4) - 1) and (((n^2) / 4) + 1).
    #State of the program after the if-else block has been executed: *n is a positive integer. If n is less than or equal to 2, the program does not change the state of any variables. If n is a positive odd integer larger than 2, the program calculates and prints two sets of values: ((n^2 - 1) / 2), ((n^2 + 1) / 2), (((n^2) / 4) - 1), and (((n^2) / 4) + 1).
#Overall this is what the function does:The function `func` reads an integer `n` from the user and performs different calculations based on the value of `n`. If `n` is less than or equal to 2, it prints -1. If `n` is a positive odd integer larger than 2, it calculates and prints two sets of values: ((n^2 - 1) / 2), ((n^2 + 1) / 2), (((n^2) / 4) - 1), and (((n^2) / 4) + 1). However, it does not return any specific output.

