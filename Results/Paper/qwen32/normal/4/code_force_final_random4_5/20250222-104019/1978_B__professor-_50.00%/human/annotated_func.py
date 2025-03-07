#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. Each of the following t test cases consists of three integers n, a, and b, where 1 <= n, a, b <= 10^9.
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
        
    #State: `t` is 0, representing that all test cases have been processed; `n`, `a`, and `b` are the last set of integers input from the user for the final test case. The final output is printed based on the last test case's values of `n`, `a`, and `b`.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of three integers `n`, `a`, and `b`. For each test case, it calculates and prints a specific integer value based on the relationships between `n`, `a`, and `b`.

