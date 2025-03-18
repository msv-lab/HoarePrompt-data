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
        #State of the program after the if-else block has been executed: *`n`, `k`, `t` are assigned values `n'`, `k'`, `t'` respectively, where 1 ≤ n' ≤ 10^9, 1 ≤ k' ≤ n', and 1 ≤ t' < n' + k'. If `t'` is less than or equal to `n'`, then `k'` has been printed. If `t'` is greater than `n'`, the printed value will be `n' + k' - t'` (which is a negative value).
    #State of the program after the if-else block has been executed: Postcondition: ***`n`, `k`, `t` are assigned values `n'`, `k'`, `t'` respectively, where 1 ≤ n' ≤ 10^9, 1 ≤ k' ≤ n', and 1 ≤ t' < n' + k'. If `t'` is less than or equal to `k'`, then `t` is printed. Otherwise, if `t'` is less than or equal to `n'`, `k'` is printed. If `t'` is greater than `n'`, the printed value will be `n' + k' - t'`, which is a negative value.*
#Overall this is what the function does:The function accepts three integer parameters `n`, `k`, and `t`, with constraints 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k. It outputs the following: If `t` is less than or equal to `k`, it prints `t`. If `t` is greater than `k` but less than or equal to `n`, it prints `k`. If `t` is greater than `n`, it prints `n + k - t`. Notably, the output of `n + k - t` can potentially be a negative value if `t` is sufficiently large, which isn't addressed in the annotations.

