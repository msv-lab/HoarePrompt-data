#State of the program right berfore the function call: n and m are positive integers such that n is even and 2 <= n, m <= 10^9, and k is a non-negative integer such that 0 <= k < n * m.
def func_1(n, m, k):
    if (k < n - 1) :
        print(k + 1, 1)
    else :
        k -= n - 1
        full_rows = k // (m - 1)
        remaining_steps = k % (m - 1)
        if (full_rows % 2 == 0) :
            row = n - full_rows
            col = 2 + remaining_steps
        else :
            row = n - full_rows
            col = m - remaining_steps
        #State of the program after the if-else block has been executed: `n` is an even positive integer and `2 <= n <= 10^9`, `m` is a positive integer and `2 <= m <= 10^9`, `k` is a non-negative integer less than `n * m`, `full_rows` equals `k // (m - 1)`, `remaining_steps` equals `k % (m - 1)`. If `full_rows` is even, then `row` equals `n - full_rows` and is even, `col` equals `2 + remaining_steps`. If `full_rows` is odd, then `row` equals `n - full_rows` and is odd, `col` equals `m - remaining_steps`.
        print(row, col)
    #State of the program after the if-else block has been executed: `n` and `m` are positive integers such that `n` is even and `2 <= n, m <= 10^9`, and `k` is a non-negative integer such that `0 <= k < n * m`. If `k < n - 1`, then the value `(k + 1, 1)` has been printed. Otherwise, `full_rows` equals `k // (m - 1)`, `remaining_steps` equals `k % (m - 1)`, if `full_rows` is even, then the values of `row` equals `n - full_rows` and `col` equals `2 + remaining_steps` have been printed, if `full_rows` is odd, then the values of `row` equals `n - full_rows` and `col` equals `m - remaining_steps` have been printed.
#Overall this is what the function does:The function accepts three parameters: `n`, `m`, and `k`, where `n` is an even positive integer and `2 <= n, m <= 10^9`, and `k` is a non-negative integer less than `n * m`, and prints a pair of values based on the value of `k`: `(k + 1, 1)` if `k < n - 1`, or `(n - full_rows, 2 + remaining_steps)` if `full_rows` is even, or `(n - full_rows, m - remaining_steps)` if `full_rows` is odd, where `full_rows = k // (m - 1)` and `remaining_steps = k % (m - 1)`.

