#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three positive integers n, a, and b such that 1 ≤ n, a, b ≤ 10^9.
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
        
    #State of the program after the  for loop has been executed: `t` is an integer input from the user and must be greater than or equal to 1. After all iterations of the loop, the following conditions hold for the variables: For each iteration, if `b <= a`, the output is `n * a`. If `b > a` and `b - a >= n`, the output is `(2 * b - n + 1) * n / 2`. If `b > a` and `b - a < n`, the output is `int((b - a) / 2 * (b - a + 1) + a * n)`.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of three positive integers `n`, `a`, and `b` such that \(1 \leq n, a, b \leq 10^9\). It reads `t` test cases from the user, where `1 \leq t \leq 10^4`. For each test case, it calculates and prints a value based on the given conditions:

1. If `b <= a`, it prints `n * a`.
2. If `b > a` and `b - a >= n`, it prints \(\frac{(2 * b - n + 1) * n}{2}\).
3. If `b > a` and `b - a < n`, it prints \(\text{int}(\frac{(b - a) * (b - a + 1)}{2} + a * n)\).

After processing all test cases, the function does not return any value but prints the calculated values for each test case. The function handles all possible cases as defined in the conditions and includes the necessary calculations for each scenario.

