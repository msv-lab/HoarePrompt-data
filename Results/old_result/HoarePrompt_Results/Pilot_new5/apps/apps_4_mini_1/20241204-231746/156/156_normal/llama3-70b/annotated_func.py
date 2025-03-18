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
        #State of the program after the if-else block has been executed: *`n` is an even integer with 2 ≤ `n` ≤ 10^9, `m` is an integer with 2 ≤ `m` ≤ 10^9, and `k` is adjusted to `k % (n * 2 - 2)` and is greater than or equal to `n - 1`. If `k` is less than `n * 2 - 2,` the printed values are `(n - (k - n + 1) % (n - 1) - 1)` and `((k - n + 1) // (n - 1) + 1)`. Otherwise, `k` is at least `n * 2 - 2` while still being adjusted as described.
    #State of the program after the if-else block has been executed: *`n` is an even integer with 2 ≤ `n` ≤ 10^9, `m` is an integer with 2 ≤ `m` ≤ 10^9, and `k` is adjusted to `k % (n * 2 - 2)`. If `k` is less than `n - 1`, then `k + 1` and `1` have been printed. Otherwise, if `k` is greater than or equal to `n - 1` and less than `n * 2 - 2`, the printed values are `(n - (k - n + 1) % (n - 1) - 1)` and `((k - n + 1) // (n - 1) + 1)`. If `k` is at least `n * 2 - 2`, the adjustments to `k` are still respected as described.
#Overall this is what the function does:The function accepts integers `n` (even), `m`, and `k`, adjusts `k`, and prints specific coordinate-like values based on its adjusted value in relation to `n`. If `k` is less than `n - 1`, it prints `(k + 1, 1)`; if `k` is between `n - 1` and `n * 2 - 2`, it prints calculated values based on `k`; otherwise, it prints `(1, 2)`. The function does not return any values, only prints output.

