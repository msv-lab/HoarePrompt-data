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
        
    #State: For each of the `t` lines, the result of the calculation based on the values of `n`, `a`, and `b` is printed. If `a` is greater than or equal to `b`, the result is `n * a`. Otherwise, the result is calculated as the sum of the maximum possible sequence of `k` numbers ending at `b` and the remaining numbers multiplied by `a`.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `n`, `a`, and `b`. For each test case, it calculates and prints a value. If `a` is greater than or equal to `b`, the printed value is `n * a`. Otherwise, it calculates the sum of the maximum possible sequence of `k` numbers ending at `b` and the remaining numbers multiplied by `a`, then prints this sum.

