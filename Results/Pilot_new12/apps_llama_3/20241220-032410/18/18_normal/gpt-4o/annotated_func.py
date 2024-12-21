#State of the program right berfore the function call: n, k, and t are integers such that 1 <= n <= 10^9, 1 <= k <= n, and 1 <= t < n + k.
def func():
    n, k, t = map(int, input().split())
    if (t <= k) :
        print(t)
    else :
        if (t <= n) :
            print(k)
        else :
            print(n + k - t)
        #State of the program after the if-else block has been executed: `n`, `k`, and `t` are input integers, and `t` is greater than `k`. If `t` is less than or equal to `n`, the value of `k` is returned as output. Otherwise, `t` is greater than `n`, and the value `n + k - t` is returned as output.
    #State of the program after the if-else block has been executed: *`n`, `k`, and `t` are input integers. If `t` is less than or equal to `k`, the value of `t` has been printed. If `t` is greater than `k` but less than or equal to `n`, the function returns `k`. If `t` is greater than both `k` and `n`, the function returns `n + k - t`.
#Overall this is what the function does:The function calculates and prints an output value based on the input integers `n`, `k`, and `t`, where `1 <= n <= 10^9`, `1 <= k <= n`, and `1 <= t < n + k`. It takes no parameters but instead reads `n`, `k`, and `t` from the user input. The function returns no value but prints the result. If `t` is less than or equal to `k`, it prints `t`. If `t` is greater than `k` but less than or equal to `n`, it prints `k`. If `t` is greater than both `k` and `n`, it prints `n + k - t`. The final state of the program after it concludes is that it has printed one of these calculated values based on the input integers `n`, `k`, and `t`, and the input variables `n`, `k`, and `t` remain in the program's memory as they were read from the user input and used for the calculation.

