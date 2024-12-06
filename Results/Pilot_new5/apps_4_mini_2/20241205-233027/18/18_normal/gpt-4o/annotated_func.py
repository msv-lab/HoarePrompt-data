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
        #State of the program after the if-else block has been executed: *`n`, `k`, and `t` are integers updated from input such that 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k with t > k. If `t` is less than or equal to `n`, then `k` has been printed. Otherwise, `n` is updated to a new integer value, `k` is updated to a new integer value, `t` is updated to a new integer value with the conditions 1 ≤ t < n + k, t > k, and t > n, and the output is `n + k - t`.
    #State of the program after the if-else block has been executed: *`n`, `k`, and `t` are integers updated from input such that 1 ≤ `n` ≤ 10^9, 1 ≤ `k` ≤ `n`, and 1 ≤ `t` < `n` + `k`. If `t` is less than or equal to `k`, then `t` is printed. Otherwise, if `t` is less than or equal to `n`, `k` has been printed. If `t` is greater than `n`, then `n`, `k`, and `t` are updated again with the conditions 1 ≤ `t` < `n` + `k`, `t` > `k`, and `t` > `n`, and the output is `n + k - t`.
#Overall this is what the function does:The function accepts three integer parameters `n`, `k`, and `t`, where the constraints are 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k. It prints `t` if `t` is less than or equal to `k`. If `t` is greater than `k` but less than or equal to `n`, it prints `k`. If `t` is greater than `n`, it calculates and prints `n + k - t`. There is no return value from the function, and it does not handle cases where the input constraints are violated, such as when `t` is outside the specified range.

