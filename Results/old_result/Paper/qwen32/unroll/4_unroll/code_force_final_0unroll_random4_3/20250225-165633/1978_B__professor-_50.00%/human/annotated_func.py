#State of the program right berfore the function call: Each test case consists of three integers n, a, and b where 1 ≤ n, a, b ≤ 10^9. The function will be called multiple times with the number of test cases t (1 ≤ t ≤ 10^4).
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
        
    #State: t is 0, n, a, and b are the values from the last iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers `n`, `a`, and `b`. For each test case, it calculates and prints a specific value based on the relationships between `n`, `a`, and `b`. The final state of the program is that it has processed all test cases and printed the corresponding results.

