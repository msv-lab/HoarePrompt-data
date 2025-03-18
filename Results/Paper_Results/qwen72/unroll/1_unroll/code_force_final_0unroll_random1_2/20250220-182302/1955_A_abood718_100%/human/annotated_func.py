#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, n, a, and b are integers such that 1 <= n <= 100 and 1 <= a, b <= 30.
def func():
    for i in range(int(input())):
        A, B, C = map(int, input().split())
        
        if B * 2 < C:
            print(A * B)
        elif A % 2 == 0:
            print(int(A * C / 2))
        else:
            X = A // 2
            print(X * C + B)
        
    #State: The values of t, n, a, and b remain unchanged. The loop iterates t times, and for each iteration, it reads three integers A, B, and C from the input. Depending on the conditions, it prints either A * B, A * C / 2 (if A is even), or X * C + B (if A is odd, where X = A // 2). The final state of the loop is that the loop has completed t iterations, and the values of t, n, a, and b are still within their initial ranges.
#Overall this is what the function does:The function `func` processes `t` test cases, where `t` is an integer such that 1 <= t <= 10^4. For each test case, it reads three integers `A`, `B`, and `C` from the input, where 1 <= A, B, C <= 100. Depending on the conditions, it prints either `A * B` if `B * 2 < C`, `A * C / 2` if `A` is even, or `X * C + B` if `A` is odd (where `X = A // 2`). After processing all `t` test cases, the function completes and the values of `t`, `n`, `a`, and `b` remain unchanged.

