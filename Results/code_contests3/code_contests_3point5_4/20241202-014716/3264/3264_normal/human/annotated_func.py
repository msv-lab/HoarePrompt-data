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
        #State of the program after the if-else block has been executed: *`n` is a positive integer between 3 and 10^9. If `n` is an odd number, the output is ((n^2) - 1) / 2 and ((n^2) + 1) / 2. If `n` is an even number, no changes occur in n and the program continues as is.
    #State of the program after the if-else block has been executed: *`n` is a positive integer between 1 and 10^9. If `n` is less than or equal to 2, `n` is decreased by 1. If `n` is between 3 and 10^9, the output varies based on whether `n` is odd or even. For odd `n`, the output is ((n^2) - 1) / 2 and ((n^2) + 1) / 2. For even `n`, no changes occur in `n`.
#Overall this is what the function does:The function `func` reads an integer `n` from the user input. If `n` is less than or equal to 2, it prints -1. For `n` greater than 2, if `n` is odd, it prints ((n^2) - 1) / 2 and ((n^2) + 1) / 2. If `n` is even, it prints (n^2 / 4 - 1) and (n^2 / 4 + 1). The function does not accept any parameters and the return value is not specified.

