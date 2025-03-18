#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, and for each test case, n, a, and b are integers where 1 ≤ n, a, b ≤ 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print(b * k - k * (k - 1) // 2 + (n - k) * a)
        
    #State: The loop has executed `t` times, where `t` is the integer input initially provided. For each iteration, `n`, `a`, and `b` are integers read from input, and `k` is calculated as the minimum of `n` and `b - a`. If `b` is less than or equal to `a`, the output is `a * n`. If `b` is greater than `a`, the output is `b * k - k * (k - 1) // 2 + (n - k) * a`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `n`, `a`, and `b`. It calculates a value based on these inputs and prints the result. Specifically, if `b` is less than or equal to `a`, it prints `a * n`. Otherwise, it calculates `k` as the minimum of `n` and `b - a`, and prints `b * k - k * (k - 1) // 2 + (n - k) * a`. After processing all `t` test cases, the function completes its execution.

