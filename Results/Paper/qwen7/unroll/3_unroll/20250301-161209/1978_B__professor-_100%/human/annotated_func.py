#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and each test case consists of three positive integers n, a, and b such that 1 ≤ n, a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if b <= a:
            print(n * a)
        elif b - a >= n:
            print(int((2 * b - n + 1) * n // 2))
        else:
            print(int((b - a) * (b - a + 1) // 2 + a * n))
        
    #State: Output State: The output state will consist of a series of integers. For each test case defined by the input integer `t`, the output will be calculated based on the conditions provided within the loop. Specifically, if `b` is less than or equal to `a`, the output will be `n * a`. If `b - a` is greater than or equal to `n`, the output will be the sum of the first `n` terms of an arithmetic sequence starting from `2b - n + 1`. Otherwise, the output will be the sum of the first `(b - a)` natural numbers plus `a * n`.
    #
    #This output state will be a list of integers, one for each test case, following the logic described above.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of three positive integers `n`, `a`, and `b`. Based on the values of `n`, `a`, and `b`, the function calculates and prints an integer for each test case. Specifically, if `b` is less than or equal to `a`, it prints `n * a`. If `b - a` is greater than or equal to `n`, it prints the sum of the first `n` terms of an arithmetic sequence starting from `2b - n + 1`. Otherwise, it prints the sum of the first `(b - a)` natural numbers plus `a * n`.

