#State of the program right berfore the function call: The function should take three parameters: n, a, and b, where n, a, and b are integers such that 1 ≤ n, a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if b <= a:
            print(n * a)
        elif b - a >= n:
            print(int((2 * b - n + 1) * n / 2))
        else:
            print(int((b - a) / 2 * (b - a + 1) + a * n))
        
    #State: `t` is 0, and the loop has executed `t` times. For each iteration, `n`, `a`, and `b` were input integers. If `b <= a`, the condition `b <= a` held true, and `n * a` was printed. If `b > a` and `b - a >= n`, the condition `b - a >= n` held true, and `int((2 * b - n + 1) * n / 2)` was printed. If `b > a` and `b - a < n`, the condition `b - a < n` held true, and `int((b - a) / 2 * (b - a + 1) + a * n)` was printed.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `n`, `a`, and `b` from the input. Depending on the relationship between `a` and `b`, it prints one of three possible values: `n * a` if `b <= a`, `int((2 * b - n + 1) * n / 2)` if `b > a` and `b - a >= n`, or `int((b - a) / 2 * (b - a + 1) + a * n)` if `b > a` and `b - a < n`. After processing all test cases, the function does not return any value.

