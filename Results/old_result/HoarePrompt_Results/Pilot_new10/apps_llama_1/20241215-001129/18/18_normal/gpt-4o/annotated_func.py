#State of the program right berfore the function call: n, k, and t are integers, 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k.
def func():
    n, k, t = map(int, input().split())
    if (t <= k) :
        print(t)
    else :
        if (t <= n) :
            print(k)
        else :
            print(n + k - t)
        #State of the program after the if-else block has been executed: `n`, `k`, and `t` are integers, `n` is an integer between 1 and 10^9, `k` is an integer between 1 and `n`, `t` is an integer between 1 and `n + k - 1`, and `t` is larger than `k`. If `t` is less than or equal to `n`, the value of `k` has been printed. If `t` is larger than `n`, the value of `n + k - t` is a negative integer.
    #State of the program after the if-else block has been executed: *`n`, `k`, and `t` are integers, `n` is an integer between 1 and 10^9, `k` is an integer between 1 and `n`, `t` is an integer between 1 and `n + k - 1`. If `t` is less than or equal to `k`, the value of `t` has been printed. If `t` is larger than `k` but less than or equal to `n`, the value of `k` has been printed. If `t` is larger than `n`, the value of `n + k - t` is a negative integer, but since `n`, `k`, and `t` are returned as integers at the output state, `n + k - t` being negative indicates `t` is indeed larger than `n` as per the given conditions.
#Overall this is what the function does:The function accepts three integer parameters `n`, `k`, and `t` with specific constraints, and prints a value based on the relative values of `n`, `k`, and `t`: `t` if `t` is less than or equal to `k`, `k` if `t` is larger than `k` but less than or equal to `n`, and `n + k - t` if `t` is larger than `n`.

