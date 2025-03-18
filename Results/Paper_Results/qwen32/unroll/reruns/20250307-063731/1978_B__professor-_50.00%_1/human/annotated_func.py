#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, n, a, and b are integers such that 1 <= n, a, b <= 10^9.
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
        
    #State: `t` is unchanged, and `n`, `a`, and `b` are not defined after the loop as they are overwritten in each iteration.
#Overall this is what the function does:The function processes `t` test cases, each defined by three integers `n`, `a`, and `b`. For each test case, it computes and prints a specific value based on the relationship between `a` and `b` relative to `n`.

