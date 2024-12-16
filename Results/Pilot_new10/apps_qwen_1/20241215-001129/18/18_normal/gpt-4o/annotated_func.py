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
        #State of the program after the if-else block has been executed: *`n`, `k`, and `t` are integers. If `t` is less than or equal to `n`, the output is `k`. Otherwise, the output is `n + k - t`.
    #State of the program after the if-else block has been executed: *`n`, `k`, and `t` are integers. If `t` is less than or equal to `k`, then `t` is printed and remains less than or equal to `k`. Otherwise, if `t` is greater than `k` but less than or equal to `n + k`, the output is `k`. If `t` is greater than `n + k`, the output is `n + k - t`.
#Overall this is what the function does:The function reads three integers `n`, `k`, and `t` from input where `1 ≤ n ≤ 10^9`, `1 ≤ k ≤ n`, and `1 ≤ t < n + k`. If `t` is less than or equal to `k`, it prints `t`. If `t` is greater than `k` but less than or equal to `n`, it prints `k`. If `t` is greater than `n + k`, it prints `n + k - t`.

