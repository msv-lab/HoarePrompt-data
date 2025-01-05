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
        #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^9 and `n` is larger than 2. If `n` is an odd integer, the first value is calculated as (n * n - 1) / 2 and the second value as (n * n + 1) / 2. If `n` is an even integer, the expressions result in `k^2 - 1` and `k^2 + 1`, where `k` is equal to `n / 2`.
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^9. If `n` is less than or equal to 2, -1 is printed. Otherwise, if `n` is greater than 2, if `n` is odd, the first value is calculated as (n * n - 1) / 2 and the second value as (n * n + 1) / 2. If `n` is even, the expressions result in `k^2 - 1` and `k^2 + 1`, where `k` is equal to `n / 2`.
#Overall this is what the function does:The function accepts a positive integer `n` via user input. If `n` is less than or equal to 2, it prints `-1`. If `n` is greater than 2 and odd, it prints two values: `(n * n - 1) / 2` and `(n * n + 1) / 2`. If `n` is even, it prints `(n * n / 4 - 1)` and `(n * n / 4 + 1)`. The function does not return any values; it only prints the results.

