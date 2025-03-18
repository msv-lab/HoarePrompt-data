#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, a, and b are integers such that 1 <= n, a, b <= 10^9.
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
        
    #State: `t` is an integer such that `t` is 0; no further iterations of the loop will occur.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `n`, `a`, and `b`. For each test case, it calculates and prints a value based on the relationship between `n`, `a`, and `b`. Specifically, it prints the maximum possible sum that can be achieved by selecting `n` integers where each integer is either `a` or between `a` and `b` (inclusive), with the goal of maximizing the sum.

