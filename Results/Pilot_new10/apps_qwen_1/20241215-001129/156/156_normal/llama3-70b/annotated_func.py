#State of the program right berfore the function call: n and m are integers such that 2 ≤ n, m ≤ 10^9 and n is always even. k is an integer such that 0 ≤ k < n·m.
def func():
    n, m, k = map(int, input().split())
    k %= n * 2 - 2
    if (k < n - 1) :
        print(k + 1, 1)
    else :
        if (k < n * 2 - 2) :
            print(n - (k - n + 1) % (n - 1) - 1, (k - n + 1) // (n - 1) + 1)
        else :
            print(1, 2)
        #State of the program after the if-else block has been executed: *`n` is an integer, `m` is an integer, `k` is an integer such that \(0 \leq k < n * 2 - 2\) and `n` is even. If \(k < n * 2 - 2\), the function prints `n - (k - n + 1) % (n - 1) - 1` and `(k - n + 1) // (n - 1) + 1`. If \(k \geq n - 1\), the function does not print anything.
    #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are integers. If `k < n - 1`, the function prints `k + 1` followed by `1`. If `k >= n - 1`, the function prints `n - (k - n + 1) % (n - 1) - 1` and `(k - n + 1) // (n - 1) + 1`. In both cases, the values of `n`, `m`, and `k` remain unchanged.
#Overall this is what the function does:The function accepts three parameters `n`, `m`, and `k`, where `n` and `m` are integers such that \(2 \leq n, m \leq 10^9\) and `n` is even, and \(0 \leq k < n \cdot m\). Depending on the value of `k`, it prints specific pairs of integers. Specifically, if \(k < n - 1\), it prints `k + 1` and `1`. If \(k \geq n - 1\), it further checks the value of `k` and prints either `n - (k - n + 1) % (n - 1) - 1` and `(k - n + 1) // (n - 1) + 1`, or `1` and `2` if \(k \geq n \cdot 2 - 2\).

