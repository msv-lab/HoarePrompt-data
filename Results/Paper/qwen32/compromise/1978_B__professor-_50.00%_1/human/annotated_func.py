#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each of the following t lines contains three integers n, a, and b such that 1 <= n, a, b <= 10^9.
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
        
    #State: t lines, each containing the result of the corresponding input set based on the given conditions.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `n`, `a`, and `b`. For each test case, it calculates and prints a specific integer value based on the conditions involving `n`, `a`, and `b`. The final state of the program is that it outputs `t` lines, each corresponding to the result of the respective test case.

