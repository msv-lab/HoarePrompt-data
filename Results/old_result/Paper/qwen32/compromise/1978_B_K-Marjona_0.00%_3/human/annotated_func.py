#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, a, and b are integers such that 1 <= n, a, b <= 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: t is an integer such that 1 <= t <= 10^4. For each test case, n, a, and b are integers such that 1 <= n, a, b <= 10^9, and the results for each test case have been printed.
#Overall this is what the function does:The function processes multiple test cases, each defined by three integers `n`, `a`, and `b`. For each test case, it calculates and prints a specific value based on the relationship between `n`, `a`, and `b`. If `b` is less than or equal to `a`, it prints `a` multiplied by `n`. Otherwise, it calculates a more complex expression involving `b`, `a`, and `n`, and prints the result.

