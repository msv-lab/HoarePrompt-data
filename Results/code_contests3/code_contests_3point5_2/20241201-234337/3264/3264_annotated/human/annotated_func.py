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
        #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ n ≤ 10^9, and n is larger than 2. If n is odd, then the expressions (n * n - 1) / 2 and (n * n + 1) / 2 evaluate to specific values based on the value of n. If n is even, the result of the expression n * n / 4 - 1 and n * n / 4 + 1 are displayed.
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ n ≤ 10^9. If n ≤ 2, there is a syntax error due to missing parentheses in the print statement. If n is larger than 2, then based on the parity of n, specific expressions are evaluated. If n is odd, the expressions (n * n - 1) / 2 and (n * n + 1) / 2 give specific values. If n is even, the expressions n * n / 4 - 1 and n * n / 4 + 1 are displayed.
#Overall this is what the function does:The function `func` reads a positive integer `n` from the user input. If `n` is less than or equal to 2, it attempts to print -1 with a syntax error due to missing parentheses in the print statement. For `n` larger than 2, it calculates specific expressions based on the parity of `n`. If `n` is odd, it prints (n * n - 1) / 2 and (n * n + 1) / 2. If `n` is even, it prints n * n / 4 - 1 and n * n / 4 + 1. The function does not have a return value.

