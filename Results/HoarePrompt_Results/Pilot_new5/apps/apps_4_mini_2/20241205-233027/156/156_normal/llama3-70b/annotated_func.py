#State of the program right berfore the function call: n and m are integers such that 2 ≤ n, m ≤ 10^9 and n is always even; k is a non-negative integer such that 0 ≤ k < n·m.
def func():
    n, m, k = map(int, input().split())
    k %= n * 2 - 2
    if (k < n - 1) :
        print(k + 1, 1)
    else :
        if (k < n * 2 - 2) :
            print(n - (k - n + 1) % (n - 1) - 1, (k - n + 1) // (n - 1) + 1)
        else :
            print(1, 2)
        #State of the program after the if-else block has been executed: *`n` is a new even integer between 2 and 10^9; `m` is a new integer between 2 and 10^9; `k` is updated to `k % (n * 2 - 2)`. If `k < n * 2 - 2`, the output values are `n - (k - n + 1) % (n - 1) - 1` and `(k - n + 1) // (n - 1) + 1`. Otherwise, `k` is updated such that `k` remains less than `n·m`, is greater than or equal to `n - 1`, and is also greater than or equal to `n * 2 - 2`.
    #State of the program after the if-else block has been executed: *`n` is an even integer between 2 and 10^9, `m` is an integer between 2 and 10^9, and `k` is updated to `k % (n * 2 - 2)` where `0 ≤ k < n·m`. If `k < n - 1`, the output is `(k + 1, 1)`. Otherwise, if `k < n * 2 - 2`, the output values are `n - (k - n + 1) % (n - 1) - 1` and `(k - n + 1) // (n - 1) + 1`. If `k` is not less than `n * 2 - 2`, then `k` is updated to ensure it remains less than `n·m`, greater than or equal to `n - 1`, and greater than or equal to `n * 2 - 2.
#Overall this is what the function does:The function accepts three integer parameters: `n` (an even integer between 2 and 10^9), `m` (an integer between 2 and 10^9), and `k` (a non-negative integer such that 0 ≤ k < n·m). It calculates a modified value of `k` using `k % (n * 2 - 2)`, and based on the value of `k`, it outputs different pairs of integers. If `k` is less than `n - 1`, it outputs `(k + 1, 1)`. If `k` is less than `n * 2 - 2`, it outputs a pair calculated from `n` and `k`. If `k` is not less than `n * 2 - 2`, it outputs `(1, 2)`. The function does not handle cases where `k` could be greater than or equal to `n·m` after the modulo operation, which may not satisfy the input constraints.

