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
        
    #State: `i` is `int(input()) - 1`, `A`, `B`, and `C` are updated to the input integers for the last iteration, and `X` is set to `A // 2` if `A` is odd and `B * 2 >= C` for the last iteration.
#Overall this is what the function does:The function processes `t` test cases, where `t` is an integer such that 1 <= t <= 10^4. For each test case, it accepts three integers `A`, `B`, and `C` such that 1 <= A, B, C <= 30. The function prints a result for each test case based on the following conditions: if `B * 2 < C`, it prints `A * B`; if `A` is even, it prints `A * C / 2`; if `A` is odd and `B * 2 >= C`, it prints two lines, the first being `A // 2` and the second being `(A // 2) * C + B`. After processing all test cases, the function concludes.

