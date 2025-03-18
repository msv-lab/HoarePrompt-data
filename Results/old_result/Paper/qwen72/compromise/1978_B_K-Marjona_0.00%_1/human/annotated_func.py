#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n, a, and b are integers such that 1 ≤ n, a, b ≤ 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: The loop has finished executing for all test cases. The values of t, n, a, and b remain unchanged as they are input values for each iteration. The output for each test case is printed according to the logic inside the loop.
#Overall this is what the function does:The function `func` processes a series of test cases. It accepts an integer `t` (1 ≤ t ≤ 10^4) indicating the number of test cases. For each test case, it reads three integers `n`, `a`, and `b` (1 ≤ n, a, b ≤ 10^9) from the input. The function then calculates and prints a result for each test case based on the values of `n`, `a`, and `b`. If `b` is less than or equal to `a`, it prints `a * n`. Otherwise, it prints a value calculated using the formula `(b + (b - k + 1)) // 2 * k + (n - k) * a`, where `k` is the minimum of `n` and `b - a`. After processing all test cases, the function completes and the values of `t`, `n`, `a`, and `b` remain unchanged as they are input values.

