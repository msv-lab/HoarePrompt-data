#State of the program right berfore the function call: n and m are even integers greater than or equal to 2, and k is a non-negative integer such that 0 <= k < n * m.
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
        #State of the program after the if-else block has been executed: *`n` and `m` are even integers greater than or equal to 2, `k` is a non-negative integer such that 0 <= k < n * m - (n - 1), `full_rows` is equal to `k // (m - 1)`, and `remaining_steps` is equal to `k % (m - 1)`. If `full_rows` is even, then `row` is equal to `n - full_rows` and `col` is equal to `2 + remaining_steps`. Otherwise, if `full_rows` is odd, then `row` is an odd integer equal to `n - full_rows` and `col` is equal to `m - remaining_steps.`
        print(row, col)
    #State of the program after the if-else block has been executed: *`n` and `m` are even integers greater than or equal to 2. If `k` is a non-negative integer less than `n - 1`, then `k + 1` is printed and is greater than or equal to 1. Otherwise, `k` is a non-negative integer such that 0 <= `k` < `n * m - (n - 1)`, where `full_rows` is equal to `k // (m - 1)`, `remaining_steps` is equal to `k % (m - 1)`, `row` is equal to either `n - full_rows` or an odd integer equal to `n - full_rows` depending on whether `full_rows` is even or odd, and `col` is equal to either `2 + remaining_steps` or `m - remaining_steps` depending on the parity of `full_rows`. The values of `row` and `col` have been printed.
#Overall this is what the function does:The function accepts two even integers `n` and `m` (both greater than or equal to 2) and a non-negative integer `k` (such that 0 ≤ k < n * m). If `k` is less than `n - 1`, it prints `k + 1` and `1`. Otherwise, it calculates the number of full rows (`full_rows`) and remaining steps (`remaining_steps`) based on the value of `k`. It then determines the `row` and `col` positions to print, switching between two configurations based on whether `full_rows` is even or odd. The function prints these calculated `row` and `col` values. The function does not return any value; it only prints output.

