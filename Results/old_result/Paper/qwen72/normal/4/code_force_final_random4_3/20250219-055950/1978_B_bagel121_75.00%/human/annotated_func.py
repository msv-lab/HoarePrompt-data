#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n, a, and b are integers such that 1 ≤ n, a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if a >= b:
            print(n * a)
        else:
            k = min(b - a + 1, n)
            ans = int((b + (b - k + 1)) / 2 * k)
            p2 = (n - k) * a
            print(ans + p2)
        
    #State: `t` is 0, `n`, `a`, and `b` are input integers for each test case. For each test case, if `a` is greater than or equal to `b`, the loop prints `n * a`. If `a` is less than `b`, the loop calculates `k` as the minimum of `b - a + 1` and `n`, `ans` as the integer result of `(b + (b - k + 1)) / 2 * k`, and `p2` as `(n - k) * a`, then prints `ans + p2`.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by integers `n`, `a`, and `b` where 1 ≤ n, a, b ≤ 10^9. It reads the number of test cases `t` (1 ≤ t ≤ 10^4) and for each test case, it calculates and prints a result. If `a` is greater than or equal to `b`, the result is `n * a`. Otherwise, it calculates `k` as the minimum of `b - a + 1` and `n`, then computes `ans` as the integer result of `(b + (b - k + 1)) / 2 * k` and `p2` as `(n - k) * a`, and prints `ans + p2`. After processing all test cases, the function concludes without returning any value.

