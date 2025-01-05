#State of the program right berfore the function call: n and m are integers such that 2 ≤ n, m ≤ 10^9, n is always even, and k is a non-negative integer such that 0 ≤ k < n * m.
def func():
    n, m, k = map(int, raw_input().split())
    x = 1
    y = 1
    if (k - n <= -1) :
        print(y, k + 1)
        sys.exit()
    #State of the program after the if block has been executed: *`n` and `m` are integers assigned from `raw_input()`, `k` is assigned a value from `raw_input()`, `x` is 1, `y` is 1. If `k - n` is less than or equal to -1, `k + 1` is printed along with `y`, and the program exits.
    k -= n
    t = k / (m - 1)
    p = k % (m - 1)
    y = n - t
    x = 2 + p if t % 2 == 0 else m - p
    print(int(math.ceil(y)), int(x))
    print(y, x)
#Overall this is what the function does:The function reads three integers `n`, `m`, and `k` from input, where `n` is an even integer and `2 ≤ n, m ≤ 10^9`, and `0 ≤ k < n * m`. If `k` is less than `n`, it prints the values `y` (which is initially 1) and `k + 1`, then exits. If `k` is greater than or equal to `n`, it computes new values for `k`, `t`, `p`, `y`, and `x`, where `y` is derived based on `k` and `t`, and `x` is calculated conditionally based on the parity of `t`. Finally, it prints the ceiling of `y` and `x`, followed by the values of `y` and `x`. The function does not have a structured return but produces output based on the calculations performed.

