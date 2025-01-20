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
        #State of the program after the if-else block has been executed: *`n`, `k`, and `t` are integers such that 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k. If `t` ≤ `n`, the state remains unchanged. If `t` > `n`, the value `n + k - t` is printed.
    #State of the program after the if-else block has been executed: *`n`, `k`, and `t` are integers such that 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k, `n` is an input integer, `k` is an input integer, `t` is an input integer. If `t` ≤ `k`, `t` has been printed. If `t` > `k` and `t` ≤ `n`, the state remains unchanged. If `t` > `n`, the value `n + k - t` is printed.
#Overall this is what the function does:- The function does not handle cases where the input values do not meet the specified constraints (e.g., `t` is not within the range `1 ≤ t < n + k`). In such cases, the behavior of the function is undefined.

