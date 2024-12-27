#State of the program right berfore the function call: The function takes no explicit inputs, but it is expected to read from standard input, where the input consists of three integers n, k, and t, such that n, k, and t are positive integers, 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k.
def func():
    n, k, t = map(int, input().split())
    if (t <= k) :
        print(t)
    else :
        if (t <= n) :
            print(k)
        else :
            print(n + k - t)
        #State of the program after the if-else block has been executed: *`n` is a positive integer, 1 ≤ `n` ≤ 10^9, `k` is a positive integer, 1 ≤ `k` ≤ `n`, `t` is a positive integer, 1 ≤ `t` < `n` + `k`, and `t` is larger than `k`. If `t` is less than or equal to `n`, then `k` has been printed. Otherwise, `t` is larger than `n` and the value `n + k - t` has been printed.
    #State of the program after the if-else block has been executed: `n` is a positive integer, 1 ≤ `n` ≤ 10^9, `k` is a positive integer, 1 ≤ `k` ≤ `n`, `t` is a positive integer, 1 ≤ `t` < `n` + `k`. If `t` is less than or equal to `k`, the value of `t` has been printed and returned. If `t` is larger than `k` but less than or equal to `n`, then `k` has been printed. If `t` is larger than `n`, the value `n + k - t` has been printed.
#Overall this is what the function does:The function reads three positive integers `n`, `k`, and `t` from standard input, where `1 ≤ n ≤ 10^9`, `1 ≤ k ≤ n`, and `1 ≤ t < n + k`. It then prints a value based on the comparison of `t` with `k` and `n`. If `t` is less than or equal to `k`, it prints `t`. If `t` is greater than `k` but less than or equal to `n`, it prints `k`. If `t` is greater than `n`, it prints `n + k - t`. After execution, the function has printed a single integer value to the standard output, and the state of the program is that `n`, `k`, and `t` have been consumed from standard input, with no explicit return value. All potential cases are handled, including edge cases where `t` equals `k` or `n`, and the function does not modify the input values or maintain any internal state after execution.

