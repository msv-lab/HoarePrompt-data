#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and for each test case, n, a, and b are positive integers such that 1 ≤ n, a, b ≤ 10^9.
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
        
    #State: Output State: The output state will consist of a series of integers printed as a result of the loop's execution. For each test case specified by the initial integer `t`, the output will depend on the values of `n`, `a`, and `b` for that particular test case. If `b <= a`, it will print `n * a`. If `b - a >= n`, it will print the value of \(\frac{(2 * b - n + 1) * n}{2}\). Otherwise, it will print the value of \(\frac{(b - a) * (b - a + 1)}{2} + a * n\).
#Overall this is what the function does:The function processes a series of test cases, each consisting of three positive integers \(n\), \(a\), and \(b\) (where \(1 \leq n, a, b \leq 10^9\)). For each test case, it calculates and prints one of three possible results based on the values of \(n\), \(a\), and \(b\):

1. If \(b \leq a\), it prints \(n \times a\).
2. If \(b - a \geq n\), it prints \(\frac{(2 \times b - n + 1) \times n}{2}\).
3. Otherwise, it prints \(\frac{(b - a) \times (b - a + 1)}{2} + a \times n\).

After processing all test cases, the function outputs a series of integers corresponding to the calculated results for each test case.

