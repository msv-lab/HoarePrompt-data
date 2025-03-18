#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, a, and b are integers such that 1 <= n, a, b <= 10^9.
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
        
    #State: The loop will print `t` lines, each representing the result of the calculation based on the input values `n`, `a`, and `b` for that iteration.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `n`, `a`, and `b`. It then calculates and prints a specific value based on the relationships between `n`, `a`, and `b`. The printed value represents the result of a computation that varies depending on whether `b` is less than or equal to `a`, or if the difference between `b` and `a` is greater than or equal to `n`, or neither of these conditions.

