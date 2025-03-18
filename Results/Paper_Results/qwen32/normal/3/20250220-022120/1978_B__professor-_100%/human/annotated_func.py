#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each of the following t lines contains three integers n, a, and b such that 1 <= n, a, b <= 10^9.
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
        
    #State: The loop has finished executing `t` times, and for each iteration, it has printed a value based on the conditions involving `n`, `a`, and `b`. The values of `t`, `n`, `a`, and `b` are unchanged from their input values, except that `t` has been decremented to 0 as the loop has completed all iterations.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `n`, `a`, and `b`. It then calculates and prints a specific value based on the relationships between `n`, `a`, and `b`. The input values of `t`, `n`, `a`, and `b` remain unchanged after the function execution.

