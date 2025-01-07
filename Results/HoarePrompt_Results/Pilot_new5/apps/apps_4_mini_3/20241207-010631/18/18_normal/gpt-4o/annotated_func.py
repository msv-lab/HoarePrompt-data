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
        #State of the program after the if-else block has been executed: *`n`, `k`, `t` are input integers where 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k with t > k. If `t` is less than or equal to `n`, then `k` is printed. Otherwise, the printed result is `n + k - t`, which results in a negative integer.
    #State of the program after the if-else block has been executed: *`n`, `k`, `t` are input integers where 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k. If `t` is less than or equal to `k`, then the value of `t` is printed. Otherwise, if `t` is less than or equal to `n`, then `k` is printed. If `t` is greater than `n`, the printed result is `n + k - t`, which results in a negative integer.
#Overall this is what the function does:The function accepts three integers, n, k, and t, from user input, where 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k. It then returns the following values based on the relationship of t with k and n: if t is less than or equal to k, it returns t; if t is less than or equal to n, it returns k; if t is greater than n, it returns n + k - t, which could potentially result in a negative integer.

