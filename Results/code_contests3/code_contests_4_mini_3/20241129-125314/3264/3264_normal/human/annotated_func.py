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
        #State of the program after the if-else block has been executed: *`n` is a positive integer larger than 2. If `n` is odd, the first expression evaluates to (n * n - 1) / 2 and the second expression evaluates to (n * n + 1) / 2. If `n` is even, the first expression evaluates to k^2 - 1 and the second expression evaluates to k^2 + 1, where k is n divided by 2.
    #State of the program after the if-else block has been executed: *`n` is a positive integer. If `n` is less than or equal to 2, an error occurs due to invalid syntax in the print statement. If `n` is greater than 2 and odd, the first expression evaluates to (n * n - 1) / 2 and the second expression evaluates to (n * n + 1) / 2. If `n` is even, the first expression evaluates to k^2 - 1 and the second expression evaluates to k^2 + 1, where k is n divided by 2.
#Overall this is what the function does:The function accepts a positive integer `n` (where 1 ≤ n ≤ 10^9) as input. If `n` is less than or equal to 2, it outputs -1. If `n` is greater than 2 and odd, it calculates and prints two values: (n * n - 1) / 2 and (n * n + 1) / 2. If `n` is even, it calculates and prints two values: (n * n / 4 - 1) and (n * n / 4 + 1). Note that the function does not return any values, but rather prints the results directly.

