#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n, a, and b are integers such that 1 ≤ n, a, b ≤ 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print(b * k - k * (k - 1) // 2 + (n - k) * a)
        
    #State: The loop has finished executing all iterations, and for each test case, the output is either `a * n` if `b <= a`, or `b * k - k * (k - 1) // 2 + (n - k) * a` where `k = min(n, b - a)`. The values of `t`, `n`, `a`, and `b` are unchanged as they are input for each iteration.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by three integers `n`, `a`, and `b` (where `1 ≤ n, a, b ≤ 10^9`). For each test case, it computes and prints a result based on the following logic: if `b` is less than or equal to `a`, the result is `a * n`. Otherwise, the result is `b * k - k * (k - 1) // 2 + (n - k) * a`, where `k` is the minimum of `n` and `b - a`. The function does not return any value; it only prints the results for each test case. The state of the program after the function concludes is that all test cases have been processed and their results printed, but the input values `t`, `n`, `a`, and `b` are unchanged.

