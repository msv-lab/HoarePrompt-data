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
        #State of the program after the if-else block has been executed: *`n` is an even integer in the range [2, 10^9]; `m` is an integer in the range [2, 10^9]; `k` is a non-negative integer that after being updated to \(k \% (n \times 2 - 2)\) satisfies \(k \geq n - 1\) and \(0 \leq k < n \times 2 - 2\). If \(k < n \times 2 - 2\), the first printed value is calculated as \(n - (k - n + 1) \% (n - 1) - 1\) and the second printed value is \((k - n + 1) // (n - 1) + 1\). Otherwise, if \(k \geq n \times 2 - 2\), the values (1, 2) are printed.
    #State of the program after the if-else block has been executed: *`n` is an even integer in the range [2, 10^9]; `m` is an integer in the range [2, 10^9]; `k` is a non-negative integer such that 0 ≤ `k` < `n * 2 - 2`. If `k` is less than `n - 1`, the output is `(k + 1, 1)`. If `k` is greater than or equal to `n - 1`, given that `0 ≤ k < n * 2 - 2`, if `k < n * 2 - 2`, the first printed value is calculated as `n - (k - n + 1) % (n - 1) - 1` and the second printed value is `(k - n + 1) // (n - 1) + 1`. If `k` is equal to or greater than `n * 2 - 2`, the values (1, 2) are printed.
#Overall this is what the function does:The function accepts three integers: `n` (an even integer between 2 and 10^9), `m` (an integer between 2 and 10^9), and `k` (a non-negative integer such that 0 ≤ `k` < `n * m`). It modifies the value of `k` to `k % (n * 2 - 2)` and prints a pair of integers based on the value of `k`. If `k` is less than `n - 1`, it prints `(k + 1, 1)`. If `k` is between `n - 1` and `n * 2 - 2`, it calculates and prints two specific values based on `k`. If `k` is equal to or greater than `n * 2 - 2`, it prints `(1, 2)`.

