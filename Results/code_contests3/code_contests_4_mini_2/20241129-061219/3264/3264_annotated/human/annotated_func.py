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
        #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^9 and `n` is greater than 2. If `n` is odd, the calculated values are ((n * n) - 1) / 2 and ((n * n) + 1) / 2. If `n` is even, the outputs are `n * n / 4 - 1` and `n * n / 4 + 1.
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^9. If `n` is less than or equal to 2, the output is -1. If `n` is greater than 2 and odd, the calculated values are ((n * n) - 1) / 2 and ((n * n) + 1) / 2. If `n` is greater than 2 and even, the outputs are `n * n / 4 - 1` and `n * n / 4 + 1.
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 10^9) and returns -1 if `n` is less than or equal to 2. If `n` is greater than 2 and odd, it outputs two values: ((n * n) - 1) / 2 and ((n * n) + 1) / 2. If `n` is greater than 2 and even, it outputs two values: (n * n / 4 - 1) and (n * n / 4 + 1).

