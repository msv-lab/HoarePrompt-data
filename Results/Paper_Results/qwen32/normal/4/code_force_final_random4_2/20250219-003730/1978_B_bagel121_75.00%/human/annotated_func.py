#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each of the following t lines contains three integers n, a, and b such that 1 <= n, a, b <= 10^9.
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
        
    #State: The loop has finished executing all `t` iterations. For each set of input values `n`, `a`, and `b`, the program has printed the result based on the given logic: if `a >= b`, it printed `n * a`; otherwise, it calculated `k = min(b - a + 1, n)`, `ans = int((b + (b - k + 1)) / 2 * k)`, and `p2 = (n - k) * a`, then printed `ans + p2`. The variable `t` is now 0, and no further iterations will occur.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of three integers `n`, `a`, and `b`. For each test case, it calculates and prints a result based on the values of `n`, `a`, and `b`. If `a` is greater than or equal to `b`, it prints `n * a`. Otherwise, it calculates a specific sum involving `b` and `a` and prints the result.

