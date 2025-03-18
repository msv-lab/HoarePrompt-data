#State of the program right berfore the function call: The function should accept three parameters: n, a, and b, where n, a, and b are integers such that 1 ≤ n, a, b ≤ 10^9.
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
        
    #State: `n`, `a`, and `b` are assigned the integer values from the input, `t` is 0, and the loop has completed all iterations. If `b` is less than or equal to `a`, no changes are made to `n`, `a`, or `b` during each iteration. If `b` is greater than `a` and `b - a` is greater than or equal to `n`, no changes are made to `n`, `a`, or `b` during each iteration. If `b` is greater than `a` and `b - a` is less than `n`, no changes are made to `n`, `a`, or `b` during each iteration.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `n`, `a`, and `b` from the input, where 1 ≤ n, a, b ≤ 10^9. Depending on the values of `a` and `b`, it prints one of three possible results: `n * a` if `b` is less than or equal to `a`, `int((2 * b - n + 1) * n // 2)` if `b - a` is greater than or equal to `n`, or `int((b - a) * (b - a + 1) // 2 + a * n)` otherwise. After processing all test cases, the function completes, and the values of `n`, `a`, and `b` are no longer relevant.

