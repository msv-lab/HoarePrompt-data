#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, n, a, and b are integers such that 1 <= n, a, b <= 10^9.
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
        
    #State: The loop has executed `t` times, and for each test case, the appropriate output (either `n * a` if `a >= b`, or `ans + p2` if `a < b`) has been printed.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of three integers `n`, `a`, and `b`. For each test case, it computes and prints a value based on the relationship between `a` and `b`. If `a` is greater than or equal to `b`, it prints `n * a`. Otherwise, it calculates the sum of the first `k` terms of an arithmetic sequence starting from `b` and decreasing by 1, where `k` is the minimum of `b - a + 1` and `n`, and adds this to the product of `(n - k)` and `a`.

