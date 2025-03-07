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
        
    #State: The values of t, n, a, and b remain unchanged, as they are not modified within the loop. The loop iterates t times, and for each iteration, it reads new values for A, B, and C from the input, processes them according to the given conditions, and prints the result. After all iterations, the loop completes, and the values of t, n, a, and b are still within their initial ranges.
#Overall this is what the function does:The function processes a series of test cases defined by an integer `t` (1 <= t <= 10^4). For each test case, it reads three integers `A`, `B`, and `C` from the input. Depending on the values of `A`, `B`, and `C`, it computes and prints a result according to the following rules: if `B * 2 < C`, it prints `A * B`; if `A` is even, it prints `A * C / 2` (as an integer); if `A` is odd, it prints `X * C + B` where `X` is `A // 2`. The function does not modify the values of `t`, `n`, `a`, or `b`, and these values remain within their initial ranges after the function completes.

