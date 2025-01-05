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
        #State of the program after the if-else block has been executed: *`n` is an integer greater than 2. If `n` is odd, the output is `((n * n - 1) / 2, (n * n + 1) / 2)`. If `n` is even, the printed values are `n^2 - 1` and `n^2 + 1`.
    #State of the program after the if-else block has been executed: *`n` is an input integer. If `n` is less than or equal to 2, -1 is printed. If `n` is greater than 2 and odd, the output is `((n * n - 1) / 2, (n * n + 1) / 2)`. If `n` is greater than 2 and even, the printed values are `n^2 - 1` and `n^2 + 1`.
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 10^9). If `n` is less than or equal to 2, it prints -1. If `n` is greater than 2 and odd, it prints two values: `(n * n - 1) / 2` and `(n * n + 1) / 2`. If `n` is greater than 2 and even, it prints two values: `n^2 - 1` and `n^2 + 1`. The function does not return any value; it only prints the results directly.

