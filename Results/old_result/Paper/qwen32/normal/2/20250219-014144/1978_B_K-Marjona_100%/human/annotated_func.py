#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, a, and b are integers such that 1 <= n, a, b <= 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print(b * k - k * (k - 1) // 2 + (n - k) * a)
        
    #State: The output consists of `t` lines, each representing the result of the computation for each test case based on the given logic.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of three integers `n`, `a`, and `b`. For each test case, it computes and prints a value based on the relationship between `a` and `b`. If `b` is less than or equal to `a`, it prints `a * n`. Otherwise, it calculates and prints a more complex expression involving `n`, `a`, and `b` to determine the result.

