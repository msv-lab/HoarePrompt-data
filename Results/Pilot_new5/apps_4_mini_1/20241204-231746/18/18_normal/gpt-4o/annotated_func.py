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
        #State of the program after the if-else block has been executed: *`n`, `k`, and `t` are integers with `t` greater than `k`. If `t` is less than or equal to `n`, then `k` is printed. Otherwise, since `t` is greater than `n`, the printed value is `n + k - t`, which is less than 0.
    #State of the program after the if-else block has been executed: *`n`, `k`, and `t` are integers. If `t` is less than or equal to `k`, then `t` is printed. Otherwise, if `t` is less than or equal to `n`, `k` is printed. If `t` is greater than both `k` and `n`, then the printed value is `n + k - t`, which is less than 0.
#Overall this is what the function does:The function accepts three integer parameters `n`, `k`, and `t` (with constraints 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k) and prints the value based on the following conditions: if `t` is less than or equal to `k`, it prints `t`; if `t` is less than or equal to `n`, it prints `k`; otherwise, it prints `n + k - t`. There is no explicit return value from the function.

