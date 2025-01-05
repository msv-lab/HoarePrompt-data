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
        #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^9 and `n` > 2. If `n` is an odd integer, the results are `(n * n - 1) / 2` and `(n * n + 1) / 2`. If `n` is an even integer, the first result is `(n^2 / 4) - 1` and the second result is `(n^2 / 4) + 1`.
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^9. If `n` is in the range 1 to 2 (inclusive), there is a syntax error in the print statement. If `n` is greater than 2, and if `n` is odd, the results are `(n * n - 1) / 2` and `(n * n + 1) / 2`. If `n` is even, the first result is `(n^2 / 4) - 1` and the second result is `(n^2 / 4) + 1`.
#Overall this is what the function does:The function accepts a positive integer `n` via user input. If `n` is less than or equal to 2, it prints -1. If `n` is greater than 2 and odd, it prints two values: `(n * n - 1) / 2` and `(n * n + 1) / 2`. If `n` is even, it prints `(n^2 / 4) - 1` and `(n^2 / 4) + 1`. The function does not return any values; it only prints the results directly. There is a potential issue with the print statement when `n` is less than or equal to 2, which may lead to a syntax error.

