#State of the program right berfore the function call: t is a positive integer such that \(1 \leq t \leq 10^4\), each test case contains three integers n, k, and x such that \(1 \leq n \leq 2 \cdot 10^5\) and \(1 \leq x, k \leq n\), and an array of n integers \(a_1, a_2, \ldots, a_n\) where \(1 \leq a_i \leq 1000\). The sum of n over all test cases does not exceed \(2 \cdot 10^5\).
def func():
    R = lambda : map(int, input().split())
    t, = R()
    while t:
        t -= 1
        
        n, k, x = R()
        
        a = [0]
        
        for y in sorted(R()):
            a += a[-1] + y,
        
        print(max(2 * a[max(i, x) - x] - a[i] for i in range(n - k, n + 1)))
        
    #State of the program after the loop has been executed: `t` is 0, `n` is the final value of `n_val` after all iterations, `k` is the final value of `k_val`, `x` is the final value of `x_val`, `a` is a list starting with 0 followed by cumulative sums of the sorted values returned by `R()` for each iteration, and the final output is the maximum value of the expression `2 * a[max(i, x) - x] - a[i]` for `i` in the range from `n - k` to `n`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \(n\), \(k\), and \(x\), and an array of \(n\) integers \(a\). For each test case, it reads the input values, sorts them, computes the cumulative sums, and then calculates the maximum value of the expression \(2 \cdot a[\max(i, x) - x] - a[i]\) for \(i\) in the range from \(n - k\) to \(n\). The function prints this maximum value for each test case.

