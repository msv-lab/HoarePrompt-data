#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n, a, and b are integers such that 1 ≤ n, a, b ≤ 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print(b * k - k * (k - 1) // 2 + (n - k) * a)
        
    #State: The loop has finished executing all iterations, and the values of t, n, a, and b are unchanged. The loop prints the result of the calculation for each test case, which is either `a * n` if `b <= a`, or `b * k - k * (k - 1) // 2 + (n - k) * a` where `k = min(n, b - a)`.
#Overall this is what the function does:The function `func` reads an integer `t` from input, indicating the number of test cases. For each test case, it reads three integers `n`, `a`, and `b` from input. It calculates and prints a result for each test case based on the following logic: if `b` is less than or equal to `a`, it prints `a * n`; otherwise, it prints `b * k - k * (k - 1) // 2 + (n - k) * a`, where `k = min(n, b - a)`. After processing all test cases, the function completes, and the values of `t`, `n`, `a`, and `b` remain unchanged.

