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
        #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^9 and `n` is larger than 2. If `n` is an odd integer larger than 2, the results are 4 and 5. If `n` is an even integer, the first expression evaluates to `n * n / 4 - 1`, and the second expression evaluates to `n * n / 4 + 1.
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^9. If `n` is in the range 1 ≤ `n` ≤ 2, a syntax error occurs during execution. If `n` is larger than 2, and if `n` is odd, the results are 4 and 5. If `n` is even, the first expression evaluates to `n * n / 4 - 1`, and the second expression evaluates to `n * n / 4 + 1.
#Overall this is what the function does:The function reads a positive integer `n` from input. If `n` is less than or equal to 2, it prints `-1`. If `n` is odd and greater than 2, it prints two values: `(n * n - 1) / 2` and `(n * n + 1) / 2`. If `n` is even and greater than 2, it prints `(n * n / 4 - 1)` and `(n * n / 4 + 1)`. The function does not handle the case where `n` is not a valid input or where the input might lead to a syntax error due to the way input is read.

