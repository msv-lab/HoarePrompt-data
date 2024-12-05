#State of the program right berfore the function call: n and m are integers such that 2 ≤ n, m ≤ 10^9 and n is always even; k is a non-negative integer such that 0 ≤ k < n·m.
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
        #State of the program after the if-else block has been executed: *`n` is an even integer and `m` is an integer such that 2 ≤ `m` ≤ 10^9. If `full_rows` is even, then `row` is equal to `n - full_rows` and `col` is equal to `2 + remaining_steps`. If `full_rows` is odd, then `row` is equal to `n - full_rows` and `col` is equal to `m - remaining_steps`, where `remaining_steps` is calculated as the remainder of (k - (n - 1)) divided by (m - 1).
        print(row, col)
    #State of the program after the if-else block has been executed: *`n` is an even integer and `m` is an integer such that 2 ≤ `m` ≤ 10^9. If `k` is less than `n - 1`, then `k` is incremented by 1, making `1 ≤ k < n`. Otherwise, `row` is equal to `n - full_rows` and `col` is equal to `2 + remaining_steps` if `full_rows` is even, or `col` is equal to `m - remaining_steps` if `full_rows` is odd.
#Overall this is what the function does:The function accepts three parameters: an even integer `n`, an integer `m`, and a non-negative integer `k`. It checks if `k` is less than `n - 1` and, if so, outputs `(k + 1, 1)`. If `k` is greater than or equal to `n - 1`, it calculates the number of full rows and remaining steps based on the adjusted value of `k`. Depending on whether the number of full rows is even or odd, it computes and prints the corresponding row and column based on the given rules. The function does not return any value; instead, it prints the results directly.

