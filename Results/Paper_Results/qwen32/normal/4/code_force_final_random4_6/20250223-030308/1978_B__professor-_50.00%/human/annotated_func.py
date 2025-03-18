#State of the program right berfore the function call: Each test case consists of three integers n, a, and b where 1 ≤ n, a, b ≤ 10^9. The function will be called multiple times for different test cases, with the first input being the number of test cases t (1 ≤ t ≤ 10^4).
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if b <= a:
            print(n * a)
        elif b - a >= n:
            print(int((2 * b - n + 1) * n / 2))
        else:
            print(int((b - a) / 2 * (b - a + 1) + a * n))
        
    #State: The loop has executed `t` times, where `t` is the input integer representing the number of test cases. For each test case, integers `n`, `a`, and `b` are read from the input. The output for each test case is determined based on the conditions: if `b <= a`, the output is `n * a`; if `b - a >= n`, the output is the sum of the first `n` terms of an arithmetic sequence starting from `2 * b - n + 1` with a common difference of `-1`; otherwise, the output is the sum of the first `b - a` terms of an arithmetic sequence starting from `a` with a common difference of `1`, plus `a * n`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers `n`, `a`, and `b`. For each test case, it calculates and prints a specific value based on the relationship between `a` and `b`. If `b` is less than or equal to `a`, it prints `n` multiplied by `a`. If the difference between `b` and `a` is greater than or equal to `n`, it prints the sum of the first `n` terms of an arithmetic sequence starting from `2 * b - n + 1` with a common difference of `-1`. Otherwise, it prints the sum of the first `b - a` terms of an arithmetic sequence starting from `a` with a common difference of `1`, plus `a * n`.

