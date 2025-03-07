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
            print(X)
            print(X * C + B)
        
    #State: The values of t, n, a, and b remain unchanged. The loop prints a series of outputs based on the conditions for each test case (A, B, C). For each test case, if B * 2 < C, it prints A * B. If A is even, it prints A * C / 2. If A is odd, it prints X (A // 2) and then X * C + B.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases, and for each test case, it reads three integers `A`, `B`, and `C`. Based on the values of `A`, `B`, and `C`, the function prints one or two lines of output for each test case. If `B * 2 < C`, it prints `A * B`. If `A` is even, it prints `A * C / 2`. If `A` is odd, it prints `A // 2` followed by `(A // 2) * C + B`. The function does not return any value. The input variables `t`, `A`, `B`, and `C` are consumed during the function execution and are not modified.

