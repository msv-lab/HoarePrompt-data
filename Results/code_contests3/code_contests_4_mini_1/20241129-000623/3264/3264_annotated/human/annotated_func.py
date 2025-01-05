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
        #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ n ≤ 10^9 and n > 2. If `n` is an odd integer greater than 2, the results are (n * n - 1) / 2 and (n * n + 1) / 2. If `n` is an even integer greater than 2, the printed output is `n * n / 4 - 1` and `n * n / 4 + 1`.
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^9. If `n` is less than or equal to 2, an attempt to print -1 is made, but the syntax is incorrect. If `n` is greater than 2, if `n` is an odd integer, the results are (n * n - 1) / 2 and (n * n + 1) / 2. If `n` is an even integer, the printed output is `n * n / 4 - 1` and `n * n / 4 + 1`.
#Overall this is what the function does:The function accepts a positive integer `n` from user input and prints specific calculated values based on `n`. If `n` is less than or equal to 2, it attempts to print -1 (but the syntax is incorrect). If `n` is greater than 2 and odd, it prints two values: `(n * n - 1) / 2` and `(n * n + 1) / 2`. If `n` is greater than 2 and even, it prints `(n * n / 4 - 1)` and `(n * n / 4 + 1)`. The function does not return a value; it only performs printing operations.

