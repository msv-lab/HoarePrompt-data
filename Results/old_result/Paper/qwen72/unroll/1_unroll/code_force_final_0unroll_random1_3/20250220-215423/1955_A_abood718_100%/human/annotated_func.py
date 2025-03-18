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
        
    #State: The values of t, n, a, and b remain unchanged. The loop prints the result of the conditional logic for each test case, but does not modify the values of t, n, a, or b.
#Overall this is what the function does:The function `func` processes a series of test cases, where each test case is defined by three integers `A`, `B`, and `C`. For each test case, it computes and prints a result based on the following conditions: if `B * 2` is less than `C`, it prints `A * B`; if `A` is even, it prints `A * C / 2` (as an integer); if `A` is odd, it prints `(A // 2) * C + B`. The function does not modify the values of `t`, `n`, `a`, or `b` provided before the function call. After processing all test cases, the function concludes without returning any value.

