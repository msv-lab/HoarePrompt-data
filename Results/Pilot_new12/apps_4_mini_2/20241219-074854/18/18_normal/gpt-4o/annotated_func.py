#State of the program right berfore the function call: n, k, and t are integers such that 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k.
def func():
    n, k, t = map(int, input().split())
    if (t <= k) :
        print(t)
    else :
        if (t <= n) :
            print(k)
        else :
            print(n + k - t)
        #State of the program after the if-else block has been executed: *`n`, `k`, and `t` are integers such that 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k. If `t` is less than or equal to `n`, the value printed is `k`. Otherwise, since `t` is greater than `n`, the result is `n + k - t`.
    #State of the program after the if-else block has been executed: *`n`, `k`, and `t` are integers such that 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k. If `t` is less than or equal to `k`, the printed value is equal to `t`. If `t` is less than or equal to `n`, the printed value is `k`. Otherwise, since `t` is greater than `n`, the printed value is `n + k - t.
#Overall this is what the function does:The function reads three integers: `n`, `k`, and `t` from input, constrained by `1 ≤ n ≤ 10^9`, `1 ≤ k ≤ n`, and `1 ≤ t < n + k`. It then evaluates the value of `t` to determine what to print: if `t` is less than or equal to `k`, it prints `t`; if `t` is between `k` and `n`, it prints `k`; and if `t` exceeds `n`, it calculates and prints `n + k - t`. Thus, the function outputs a value based on these comparisons and conditions, which could represent some processed result related to `t` in the context defined by `n` and `k`. Note that the function only prints the result and does not return any values.

