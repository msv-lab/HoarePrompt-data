#State of the program right berfore the function call: n, m, a, and b are integers such that 1 ≤ n, m ≤ 10^12 and 1 ≤ a, b ≤ 100.
def func():
    n, m, a, b = map(int, input().split())

r = n % m
    if (r == 0) :
        print(0)
    else :
        if (m - r <= n) :
            print(min((m - r) * a, r * b))
        else :
            print((m - r) * a)
        #State of the program after the if-else block has been executed: *`n`, `m`, `a`, `b`, and `r` are integers where `r` is the remainder of `n` divided by `m` and `r` is not equal to 0. If `m - r` is less than or equal to `n`, the minimum value between `(m - r) * a` and `r * b` is printed. If `m - r` is greater than `n`, the value of `(m - r) * a` is printed.
    #State of the program after the if-else block has been executed: *`n`, `m`, `a`, `b`, and `r` are integers where `r` is the remainder of `n` divided by `m`. If `r` is 0, the program does nothing. If `r` is not 0, and `m - r` is less than or equal to `n`, the minimum value between `(m - r) * a` and `r * b` is printed. If `m - r` is greater than `n`, the value of `(m - r) * a` is printed.
#Overall this is what the function does:The function reads four integers `n`, `m`, `a`, and `b` from the input, where `1 ≤ n, m ≤ 10^12` and `1 ≤ a, b ≤ 100`. It calculates the remainder `r` of `n` divided by `m`. If `r` is 0, the function prints 0. Otherwise, it checks if `m - r` is less than or equal to `n`. If true, it prints the minimum value between `(m - r) * a` and `r * b`. If `m - r` is greater than `n`, it prints `(m - r) * a`. The function does not return any value; it only prints the result. Potential edge cases include when `n` is exactly divisible by `m` (i.e., `r = 0`), and when `m - r` is greater than `n`, which could occur if `n` is very small compared to `m`. The function does not handle invalid input or non-integer inputs, which could lead to runtime errors.

