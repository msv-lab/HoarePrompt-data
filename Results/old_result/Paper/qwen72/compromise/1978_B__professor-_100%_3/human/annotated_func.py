#State of the program right berfore the function call: t is an integer such that 1 \le t \le 10^4, and for each test case, n, a, and b are integers such that 1 \le n, a, b \le 10^9.
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
        
    #State: The loop has finished executing all iterations, and the values of t, n, a, and b are unchanged, but the loop has printed the results of the calculations for each test case according to the given conditions.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `n`, `a`, and `b` from the input. Depending on the relationship between `a` and `b`, it calculates and prints one of three possible results: `n * a` if `b <= a`, `int((2 * b - n + 1) * n // 2)` if `b - a >= n`, or `int((b - a) * (b - a + 1) // 2 + a * n)` otherwise. After processing all test cases, the function concludes, and the values of `t`, `n`, `a`, and `b` are unchanged.

