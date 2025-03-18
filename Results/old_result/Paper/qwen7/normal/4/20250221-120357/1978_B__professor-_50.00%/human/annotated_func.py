#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are positive integers such that 1 ≤ n, a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if b <= a:
            print(n * a)
        elif b - a >= n:
            print(int((2 * b - n + 1) * n / 2))
        else:
            print(int((b - a) / 2 * (b - a + 1) + a * n))
        
    #State: `t` is a positive integer such that \(1 \leq t < 10^4\), `_` is `t`, `n` is the first integer from the input, `a` is the second integer from the input, `b` is the third integer from the input. The values of `t`, `_`, `n`, `a`, and `b` remain unchanged after all iterations of the loop.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \(n\), \(a\), and \(b\). For each test case, it calculates and prints one of three possible results based on the values of \(n\), \(a\), and \(b\). If \(b \leq a\), it prints \(n \times a\). If \(b - a \geq n\), it prints \(\frac{(2 \times b - n + 1) \times n}{2}\). Otherwise, it prints \(\frac{(b - a) \times (b - a + 1)}{2} + a \times n\). The function does not return any value but outputs the calculated results for each test case.

