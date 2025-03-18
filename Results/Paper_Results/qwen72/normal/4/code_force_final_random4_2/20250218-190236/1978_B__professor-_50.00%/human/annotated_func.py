#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n, a, and b are integers such that 1 ≤ n, a, b ≤ 10^9.
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
        
    #State: `t` is 0, `n`, `a`, and `b` are input integers for each iteration. For each iteration, if `b` is less than or equal to `a`, the loop prints `n * a`. If `b` is greater than `a` and the difference between `b` and `a` is greater than or equal to `n`, the loop prints `int((2 * b - n + 1) * n / 2)`. If `b` is greater than `a` and the difference between `b` and `a` is less than `n`, the loop prints `int((b - a) / 2 * (b - a + 1) + a * n)`.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `n`, `a`, and `b` from the input. Depending on the values of `a` and `b`, it prints one of three possible results: `n * a` if `b` is less than or equal to `a`, `int((2 * b - n + 1) * n / 2)` if `b` is greater than `a` and the difference between `b` and `a` is greater than or equal to `n`, or `int((b - a) / 2 * (b - a + 1) + a * n)` if `b` is greater than `a` and the difference between `b` and `a` is less than `n`. After processing all `t` test cases, the function concludes. The final state of the program is that `t` is 0, and the values of `n`, `a`, and `b` are undefined as they are re-assigned in each iteration.

