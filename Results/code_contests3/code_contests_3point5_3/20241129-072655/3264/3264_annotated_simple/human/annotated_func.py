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
        #State of the program after the if-else block has been executed: *`n` is a positive odd integer, such that 1 ≤ n ≤ 10^9 and n is greater than 2. If n is odd, the results are (n^2 - 1) / 2 and (n^2 + 1) / 2. If n is not odd, the result of the expression is n * n / 4 - 1 and n * n / 4 + 1.
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ n ≤ 10^9. If n ≤ 2, the program does not change the state. If n is a positive odd integer greater than 2, the results are (n^2 - 1) / 2 and (n^2 + 1) / 2. If n is not odd, the results are n * n / 4 - 1 and n * n / 4 + 1.
#Overall this is what the function does:The function `func` reads an integer `n` from the user input. If `n` is less than or equal to 2, it prints -1. If `n` is a positive odd integer greater than 2, it prints the results of the expressions ((n^2 - 1) / 2) and ((n^2 + 1) / 2). If `n` is not an odd integer, it prints the results of the expressions (n * n / 4 - 1) and (n * n / 4 + 1).

