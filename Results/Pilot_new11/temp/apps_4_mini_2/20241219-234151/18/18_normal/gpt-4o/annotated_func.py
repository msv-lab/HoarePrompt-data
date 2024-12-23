#State of the program right berfore the function call: n, k, and t are positive integers such that 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k.
def func():
    n, k, t = map(int, input().split())
    if (t <= k) :
        print(t)
    else :
        if (t <= n) :
            print(k)
        else :
            print(n + k - t)
        #State of the program after the if-else block has been executed: *`n`, `k`, and `t` are positive integers that satisfy the conditions 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k; if `t` is less than or equal to `n`, the value of `k` is printed. Otherwise, the expression `n + k - t` is printed.
    #State of the program after the if-else block has been executed: *`n`, `k`, and `t` are positive integers that satisfy the conditions 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k. If `t` is less than or equal to `k`, the value of `t` is printed. If `t` is less than or equal to `n`, the value of `k` is printed. Otherwise, the expression `n + k - t` is printed.
#Overall this is what the function does:The function takes three positive integer inputs, `n`, `k`, and `t`, satisfying the constraints 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k. It evaluates the value of `t` against `k` and `n` to determine what to print: if `t` is less than or equal to `k`, it prints `t`; if `t` is greater than `k` but less than or equal to `n`, it prints `k`; and if `t` exceeds `n`, it prints `n + k - t`. The function does not return a value; instead, it outputs the result directly to the standard output based on these conditions. Importantly, the function exclusively prints results and does not store or return these values, which should be noted when considering its overall behavior.

