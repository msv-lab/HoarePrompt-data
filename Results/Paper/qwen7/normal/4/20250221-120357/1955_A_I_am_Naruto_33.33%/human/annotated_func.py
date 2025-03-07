#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n > 1:
            ans1 = a * n
            ans2 = b * n // 2 + a * n % 2
            print(min(ans1, ans2))
        else:
            print(a)
        
    #State: After the loop executes all iterations, `t` is a positive integer such that \(1 \leq t \leq 10^4\). For each test case, `n`, `a`, and `b` are integers such that \(1 \leq n \leq 100\) and \(1 \leq a, b \leq 30\). The variable `ans1` will hold the value of `a * n` if `n > 1`, otherwise it remains unchanged. Similarly, `ans2` will hold the value of `b * n // 2 + a * n % 2` if `n > 1`, otherwise it remains unchanged.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \(n\), \(a\), and \(b\). For each test case, it calculates either \(a \times n\) or \(b \times \frac{n}{2} + a \times (n \mod 2)\) based on whether \(n > 1\). It then prints the minimum of these two values. If \(n = 1\), it simply prints \(a\). The function reads \(t\) test cases from the input, where \(1 \leq t \leq 10^4\).

