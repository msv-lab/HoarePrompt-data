#State of the program right berfore the function call: Each test case consists of three integers n, a, and b where 1 ≤ n, a, b ≤ 10^9. There are t test cases where 1 ≤ t ≤ 10^4.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print(b * k - k * (k - 1) // 2 + (n - k) * a)
        
    #State: The output state consists of `t` lines, where each line is the result of the computation for each test case. For each test case, if `b` is less than or equal to `a`, the output is `a * n`. Otherwise, the output is `b * k - k * (k - 1) // 2 + (n - k) * a`, where `k` is the minimum of `n` and `b - a`.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `n`, `a`, and `b`. For each test case, it computes and prints a value based on the relationship between `a` and `b`. If `b` is less than or equal to `a`, it prints `a * n`. Otherwise, it calculates a more complex expression involving `b`, `a`, and the minimum of `n` and `b - a`, and prints the result.

