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
        #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^9 and `n` is larger than 2. If `n` is an odd number, the expressions evaluate to (n * n - 1) / 2 and (n * n + 1) / 2. If `n` is an even number, the results of the expressions are `n * n / 4 - 1` and `n * n / 4 + 1`.
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^9. If `n` is less than or equal to 2, the output is -1. If `n` is larger than 2 and odd, the expressions evaluate to (n * n - 1) / 2 and (n * n + 1) / 2. If `n` is even, the results of the expressions are `n * n / 4 - 1` and `n * n / 4 + 1`.
#Overall this is what the function does:The function reads a positive integer `n` from input, which must be between 1 and 10^9. If `n` is less than or equal to 2, it prints -1. If `n` is odd, it calculates and prints the values `(n * n - 1) / 2` and `(n * n + 1) / 2`. If `n` is even, it calculates and prints `n * n / 4 - 1` and `n * n / 4 + 1`. Thus, the function handles different cases based on the parity of `n` and outputs specific values accordingly.

