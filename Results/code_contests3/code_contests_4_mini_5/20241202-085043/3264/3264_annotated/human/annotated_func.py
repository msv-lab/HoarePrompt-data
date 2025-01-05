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
        #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^9 and `n` > 2. If `n` is odd, the outputs are (n * n - 1) / 2 and (n * n + 1) / 2. If `n` is even, the outputs are `k^2 - 1` and `k^2 + 1`, where `k` is half of `n`.
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^9. If `n` ≤ 2, a syntax error occurs and no output is produced. If `n` > 2 and is odd, the outputs are (n * n - 1) / 2 and (n * n + 1) / 2. If `n` > 2 and is even, the outputs are `k^2 - 1` and `k^2 + 1`, where `k` is half of `n`.
#Overall this is what the function does:The function accepts a positive integer `n` via user input. If `n` is less than or equal to 2, it prints -1. If `n` is odd and greater than 2, it prints two values: `(n * n - 1) / 2` and `(n * n + 1) / 2`. If `n` is even and greater than 2, it prints two values: `n * n / 4 - 1` and `n * n / 4 + 1`. The function does not return any values, and there is a potential issue with how the output is formatted due to the lack of parentheses in the print statements.

