#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, n, a, and b are integers such that 1 <= n, a, b <= 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print(b * k - k * (k - 1) // 2 + (n - k) * a)
        
    #State: The loop has executed all iterations, and the values of t, n, a, and b remain unchanged as they were input for each test case. The loop prints the calculated value for each test case, which is either `a * n` if `b <= a`, or `b * k - k * (k - 1) // 2 + (n - k) * a` where `k = min(n, b - a)`.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by three integers `n`, `a`, and `b` within the range 1 to 10^9. For each test case, it calculates and prints a value based on the following logic: if `b` is less than or equal to `a`, it prints `a * n`; otherwise, it prints `b * k - k * (k - 1) // 2 + (n - k) * a`, where `k` is the minimum of `n` and `b - a`. The function does not return any value; it only prints the results for each test case. The input variables `t`, `n`, `a`, and `b` remain unchanged after the function execution.

