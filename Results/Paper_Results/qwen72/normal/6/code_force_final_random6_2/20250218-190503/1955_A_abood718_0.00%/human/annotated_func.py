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
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n`, `a`, and `b` are integers such that 1 <= n <= 100 and 1 <= a, b <= 30, `i` is `int(input()) - 1`, `A` is an integer input, `B` is an integer input, `C` is an integer input. If `B * 2 < C`, the state of the variables remains unchanged. If `B * 2 >= C` and `A` is even, the state of the variables remains unchanged. If `B * 2 >= C` and `A` is odd, `X` is set to `A // 2`.
#Overall this is what the function does:The function processes `t` test cases, where `t` is an integer such that 1 <= t <= 10^4. For each test case, it accepts three integers `A`, `B`, and `C` such that 1 <= A, B, C <= 30. If `B * 2 < C`, it prints `A * B`. If `A` is even, it prints `A * C / 2`. If `A` is odd, it prints two values: `A // 2` and `A // 2 * C + B`. The function does not return any values; it only prints the results for each test case.

