#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each of the following t test cases consists of three integers n, a, and b such that 1 <= n, a, b <= 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if b <= a:
            print(n * a)
        elif b - a >= n:
            print(int((2 * b - n + 1) * n // 2))
        else:
            print(int((b - a) * (b - a + 1) // 2 + a * n))
        
    #State: The output state consists of `t` lines, each representing the result of the expression evaluated for each set of `n`, `a`, and `b` read from the input. Specifically, for each iteration, if `b <= a`, the result is `n * a`. If `b - a >= n`, the result is the integer value of `(2 * b - n + 1) * n // 2`. Otherwise, the result is the integer value of `(b - a) * (b - a + 1) // 2 + a * n`. The values of `t`, `n`, `a`, and `b` from the initial state remain unchanged except that `t` iterations of the loop have been executed, and the results have been printed.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `n`, `a`, and `b`. For each test case, it computes and prints a specific result based on the values of `a` and `b` relative to `n`. If `b` is less than or equal to `a`, the result is `n * a`. If the difference `b - a` is greater than or equal to `n`, the result is calculated using the formula `(2 * b - n + 1) * n // 2`. Otherwise, the result is calculated using the formula `(b - a) * (b - a + 1) // 2 + a * n`.

