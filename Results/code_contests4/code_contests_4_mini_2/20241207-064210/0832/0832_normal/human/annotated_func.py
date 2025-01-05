#State of the program right berfore the function call: n and m are integers such that 2 ≤ n, m ≤ 10^9 and n is always even; k is a non-negative integer such that 0 ≤ k < n·m.
def func():
    n, m, k = map(int, raw_input().split())
    x = 1
    y = 1
    if (k - n <= -1) :
        print(y, k + 1)
        sys.exit()
    #State of the program after the if block has been executed: *`n`, `m`, `k` are input integers, `x` is 1, and `y` is 1. If `k - n` is less than or equal to -1, the program execution is terminated without printing anything.
    k -= n
    t = k / (m - 1)
    p = k % (m - 1)
    y = n - t
    x = 2 + p if t % 2 == 0 else m - p
    print(int(math.ceil(y)), int(x))
    print(y, x)
#Overall this is what the function does:The function accepts three integers `n`, `m`, and `k`, where `n` is even, and `k` is a non-negative integer. It first checks if `k` is less than `n`, and if so, it prints `(1, k+1)` and terminates the program. If `k` is greater than or equal to `n`, it calculates values `t` and `p` based on `(k - n)` and updates `y` and `x` using these calculations. Finally, it prints the values of `y` and `x`. The function does not return any values but prints two lines of output based on the calculations performed. It does not handle cases where `k` is less than `n` in a way that allows further execution beyond the initial print and exit.

