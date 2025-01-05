#State of the program right berfore the function call: n and m are even integers such that 2 <= n, m <= 109 and 0 <= k < n*m.**
def func():
    n, m, k = map(int, raw_input().split())
    x = 1
    y = 1
    if (k - n <= -1) :
        print(y, k + 1)
        sys.exit()
    #State of the program after the if block has been executed: *`n` and `m` are even integers such that 2 <= n, m <= 109; `k` is a non-negative integer less than n*m; `x` is 1, `y` is 1. If k - n <= -1, then the value of `k` is less than `n`, the value of `m` is unchanged, and the program has exited using `sys.exit()` without printing `y` and `k + 1`.
    k -= n
    t = k / (m - 1)
    p = k % (m - 1)
    y = n - t
    x = 2 + p if t % 2 == 0 else m - p
    print(int(math.ceil(y)), int(x))
    print(y, x)
#Overall this is what the function does:The function `func` reads three integers n, m, and k from the user input. It then performs calculations based on these inputs to determine new values for y and x. The function prints the values of y and x after the computations. If k - n is less than or equal to -1, the function prints y and k + 1 without performing further calculations and exits the program. The function does not return any value.

