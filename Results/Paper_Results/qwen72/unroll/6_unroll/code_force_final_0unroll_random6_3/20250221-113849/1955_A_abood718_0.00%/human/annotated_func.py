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
        
    #State: The loop executes t times, and for each iteration, it reads three integers A, B, and C from the input. Depending on the conditions, it prints either A * B, A * C / 2 (if A is even), or X (A // 2) followed by X * C + B (if A is odd). The values of t, n, a, and b remain unchanged as they are not modified within the loop.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by three integers `A`, `B`, and `C`. It reads the number of test cases `t` from the input, where `1 <= t <= 10^4`. For each test case, it reads `A`, `B`, and `C` from the input, and based on the conditions, it prints either `A * B`, `A * C / 2` (if `A` is even), or `X` followed by `X * C + B` (if `A` is odd, where `X = A // 2`). The function does not return any value; it only prints the results to the console. The values of `t`, `n`, `a`, and `b` remain unchanged as they are not modified within the function.

