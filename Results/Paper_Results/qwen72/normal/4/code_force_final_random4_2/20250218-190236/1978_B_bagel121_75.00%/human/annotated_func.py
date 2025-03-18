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
        
    #State: `t` is 0, `n`, `a`, and `b` are input integers for each test case. If `a` is greater than or equal to `b`, no changes are made to `a`, `b`, or `n`. If `a` is less than `b`, `k` is the minimum value between `b - a + 1` and `n`, `ans` is the integer value of `(b + (b - k + 1)) / 2 * k`, and `p2` is the integer value of `(n - k) * a`.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `n`, `a`, and `b` from the input. If `a` is greater than or equal to `b`, it prints `n * a`. If `a` is less than `b`, it calculates and prints a value that is the sum of `k` terms of an arithmetic sequence starting from `b` and decreasing by 1, plus `(n - k) * a`, where `k` is the minimum of `b - a + 1` and `n`. After processing all test cases, the function concludes with `t` being 0, and the input variables `n`, `a`, and `b` are no longer relevant.

