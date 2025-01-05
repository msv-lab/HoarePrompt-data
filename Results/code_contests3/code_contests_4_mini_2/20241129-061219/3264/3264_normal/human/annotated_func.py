#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9.
def func():
    n = int(raw_input())
    if (n <= 2) :
        print - 1
    else :
        if (n & 1) :
            print(n * n - 1) / 2, (n * n + 1) / 2
        else :
            print(n * n / 4 - 1), n * n / 4 + 1
        #State of the program after the if-else block has been executed: *`n` is a positive integer between 1 and 10^9 and larger than 2. If `n` is odd, the results are \((n^2 - 1) / 2\) and \((n^2 + 1) / 2\). If `n` is even, the results are \((n^2 / 4 - 1)\) and \((n^2 / 4 + 1)\).
    #State of the program after the if-else block has been executed: *`n` is a positive integer between 1 and 10^9. If `n` is less than or equal to 2, a syntax error occurs due to an incorrect print statement. If `n` is larger than 2 and odd, the results are \((n^2 - 1) / 2\) and \((n^2 + 1) / 2\). If `n` is larger than 2 and even, the results are \((n^2 / 4 - 1)\) and \((n^2 / 4 + 1)\).
#Overall this is what the function does:Functionality: ** The function reads a positive integer `n` from standard input. If `n` is less than or equal to 2, it outputs -1. If `n` is greater than 2 and odd, it calculates and prints two values: \((n^2 - 1) / 2\) and \((n^2 + 1) / 2\). If `n` is greater than 2 and even, it prints \((n^2 / 4 - 1)\) and \((n^2 / 4 + 1)\). The function does not return any value; instead, it directly prints the results to the standard output.

