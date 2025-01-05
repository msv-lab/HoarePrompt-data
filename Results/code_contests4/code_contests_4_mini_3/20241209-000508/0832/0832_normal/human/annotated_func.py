#State of the program right berfore the function call: n and m are integers such that 2 ≤ n, m ≤ 10^9 (n is always even), and k is a non-negative integer such that 0 ≤ k < n * m.
def func():
    n, m, k = map(int, raw_input().split())
    x = 1
    y = 1
    if (k - n <= -1) :
        print(y, k + 1)
        sys.exit()
    #State of the program after the if block has been executed: *`n` and `m` are integers such that 2 ≤ `n` ≤ 10^9 and 2 ≤ `m` ≤ 10^9; `k` is a non-negative integer such that 0 ≤ `k` < `n` * `m` and `k` ≤ `n - 1. If `k` is less than `n`, `y` remains 1, and the output printed is (1, k + 1), after which the program terminates due to sys.exit().
    k -= n
    t = k / (m - 1)
    p = k % (m - 1)
    y = n - t
    x = 2 + p if t % 2 == 0 else m - p
    print(int(math.ceil(y)), int(x))
    print(y, x)
#Overall this is what the function does:The function accepts no direct parameters but reads integers `n`, `m`, and `k` from input, where `n` is an even integer and both `n` and `m` are in the range [2, 10^9], while `k` is a non-negative integer such that 0 ≤ `k` < n * m. The function first checks if `k` is less than `n`, and if so, it prints (1, k + 1) and exits. If `k` is greater than or equal to `n`, it calculates new values for `y` and `x` based on the adjusted value of `k` and then prints them. The function does not handle cases where `k` may equal or exceed `n * m`, as the input constraints ensure `k` is always less than this value.

