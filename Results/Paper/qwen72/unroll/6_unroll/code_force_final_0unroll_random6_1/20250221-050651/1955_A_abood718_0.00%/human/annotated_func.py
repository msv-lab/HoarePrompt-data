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
        
    #State: The values of t, n, a, and b remain unchanged. The loop iterates t times, and for each iteration, it reads three integers A, B, and C from the input. Depending on the conditions, it prints either A * B, A * C / 2, or two lines: X and X * C + B, where X is A // 2. The specific output for each iteration depends on the input values of A, B, and C.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `A`, `B`, and `C` from the input. Depending on the values of `A`, `B`, and `C`, it prints either `A * B`, `A * C / 2` (if `A` is even), or two lines: `X` and `X * C + B` (if `A` is odd, where `X` is `A // 2`). The function does not return any value; it only prints the results to the console. The values of `t`, `A`, `B`, and `C` are not modified and remain as they were read from the input.

