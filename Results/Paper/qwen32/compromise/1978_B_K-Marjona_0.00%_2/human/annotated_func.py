#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, n, a, and b are integers such that 1 <= n, a, b <= 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: The variable t remains unchanged, and for each test case, the result of the expression is printed: if b <= a, a * n is printed; otherwise, (b + (b - k + 1)) // 2 * k + (n - k) * a is printed, where k is the minimum of n and b - a.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of three integers `n`, `a`, and `b`. For each test case, it computes and prints a result based on the values of `n`, `a`, and `b`. Specifically, if `b` is less than or equal to `a`, it prints `a * n`. Otherwise, it calculates and prints a more complex expression involving `b`, `a`, and `n`.

