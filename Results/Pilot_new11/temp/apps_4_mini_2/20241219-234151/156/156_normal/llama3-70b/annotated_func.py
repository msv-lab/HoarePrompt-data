#State of the program right berfore the function call: n and m are integers such that 2 ≤ n, m ≤ 10^9 and n is even; k is a non-negative integer such that 0 ≤ k < n·m.
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
        #State of the program after the if-else block has been executed: *`n` is an even integer within the range of `2 ≤ n ≤ 10^9`, `m` is an integer within the same range, and `k` is an integer such that `0 ≤ k < n · m` and `k ≥ n - 1`. If `k < n * 2 - 2`, the first output is `n - (k - n + 1) % (n - 1) - 1` and the second output is `(k - n + 1) // (n - 1) + 1`. Otherwise, the outputs are 1 and 2.
    #State of the program after the if-else block has been executed: *`n` is an even integer within the range of `2 ≤ n ≤ 10^9`, and `m` is an integer within the same range. If `k` is less than `n - 1`, then 'k + 1' has been printed alongside '1'. If `k` is greater than or equal to `n - 1`, and `k` is less than `n * 2 - 2`, the first output will be `n - (k - n + 1) % (n - 1) - 1` and the second output will be `(k - n + 1) // (n - 1) + 1`. If `k` is greater than or equal to `n - 1` and `k` is greater than or equal to `n * 2 - 2`, the outputs will be 1 and 2.
#Overall this is what the function does:The function reads three integers, `n`, `m`, and `k` from input, where `n` is an even integer between 2 and 10^9, `m` is between 2 and 10^9, and `k` is a non-negative integer less than `n * m`. It then calculates a modified value of `k` (using `k % (n * 2 - 2)`) and determines which coordinates to print based on the value of `k`. Specifically, if `k` is less than `n - 1`, it outputs the coordinates `(k + 1, 1)`. If `k` falls within the range `[n - 1, n * 2 - 2)`, it computes and prints coordinates derived from the modified `k`. If `k` is greater than or equal to `n * 2 - 2`, it outputs the fixed coordinates `(1, 2)`. Therefore, the function effectively translates the input `k` into specific (1-indexed) grid coordinates based on the conditions outlined, handling edge cases appropriately but not performing any additional validation or safeguards against invalid inputs beyond those specified.

