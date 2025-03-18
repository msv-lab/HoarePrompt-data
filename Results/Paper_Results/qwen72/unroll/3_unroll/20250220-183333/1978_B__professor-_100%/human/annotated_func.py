#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, n, a, and b are integers such that 1 <= n, a, b <= 10^9.
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
        
    #State: The loop has finished executing for all t test cases, and the output for each test case is determined based on the conditions provided in the loop body. The values of t, n, a, and b are not retained after the loop, as they are input values and local to each iteration.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `n`, `a`, and `b` from the input. Based on the values of `a` and `b`, it calculates and prints a result for each test case. The result is determined as follows: if `b` is less than or equal to `a`, it prints `n * a`; if `b - a` is greater than or equal to `n`, it prints `int((2 * b - n + 1) * n // 2)`; otherwise, it prints `int((b - a) * (b - a + 1) // 2 + a * n). After processing all test cases, the function concludes, and the values of `t`, `n`, `a`, and `b` are not retained.

