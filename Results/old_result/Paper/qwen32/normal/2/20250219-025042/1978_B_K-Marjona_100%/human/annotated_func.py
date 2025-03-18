#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, a, and b are integers such that 1 <= n, a, b <= 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print(b * k - k * (k - 1) // 2 + (n - k) * a)
        
    #State: t is 0, and no more inputs are processed.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of three integers `n`, `a`, and `b`. For each test case, it computes and prints a specific value based on the relationship between `a` and `b` and the count `n`. If `b` is less than or equal to `a`, it prints `a` multiplied by `n`. Otherwise, it calculates a more complex expression involving `b`, `a`, and `n` and prints the result.

