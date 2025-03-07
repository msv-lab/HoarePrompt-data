#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and each test case consists of three positive integers n, a, and b such that 1 ≤ n, a, b ≤ 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print(b * k - k * (k - 1) // 2 + (n - k) * a)
        
    #State: Output State: The output state consists of multiple lines, where each line corresponds to the output of one test case. For each test case, if \(b \leq a\), the output is \(a \times n\). Otherwise, the output is \(b \times k - \frac{k \times (k - 1)}{2} + (n - k) \times a\), with \(k = \min(n, b - a)\).
    #
    #This means for each test case, the output will either be a simple multiplication of \(a\) and \(n\) or a more complex calculation involving \(b\), \(a\), and \(k\), depending on the conditions specified in the loop.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of three positive integers `n`, `a`, and `b`. For each test case, it calculates and prints either `a * n` or `b * k - k * (k - 1) / 2 + (n - k) * a`, depending on whether `b` is less than or equal to `a`. Here, `k` is defined as the minimum of `n` and `b - a`. The function does not return any value but outputs the results for each test case.

