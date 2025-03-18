#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, n, a, and b are integers such that 1 <= n, a, b <= 10^9.
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
        
    #State: The loop has finished executing for all `t` test cases, and for each test case, the output is either `n * a` if `a >= b`, or the sum of `ans` and `p2` where `ans` is the sum of the first `k` integers starting from `b` and `p2` is `(n - k) * a` if `a < b`. The values of `t`, `n`, `a`, and `b` for each test case are unchanged, but the loop has completed its iterations.
#Overall this is what the function does:The function `func` processes `t` test cases, where `t` is an integer between 1 and 10^4. For each test case, it reads three integers `n`, `a`, and `b`, each between 1 and 10^9. If `a` is greater than or equal to `b`, it prints `n * a`. Otherwise, it calculates a value `ans` as the sum of the first `k` integers starting from `b`, where `k` is the minimum of `b - a + 1` and `n`. It also calculates `p2` as `(n - k) * a`. The function then prints the sum of `ans` and `p2`. After processing all test cases, the function completes and the values of `t`, `n`, `a`, and `b` for each test case remain unchanged.

