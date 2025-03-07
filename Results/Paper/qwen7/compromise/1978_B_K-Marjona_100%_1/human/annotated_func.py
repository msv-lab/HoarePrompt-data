#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and for each test case, n, a, and b are positive integers such that 1 ≤ n, a, b ≤ 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print(b * k - k * (k - 1) // 2 + (n - k) * a)
        
    #State: Output State: The output state consists of multiple lines, where each line corresponds to the output of one test case. For each test case, if \( b \leq a \), the output is \( a \times n \). Otherwise, the output is \( b \times k - \frac{k \times (k - 1)}{2} + (n - k) \times a \), with \( k = \min(n, b - a) \).
    #
    #This means that for each test case, the program calculates either \( a \times n \) or \( b \times k - \frac{k \times (k - 1)}{2} + (n - k) \times a \) based on the conditions given, and prints these values in separate lines.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it reads three positive integers `n`, `a`, and `b` (where 1 ≤ n, a, b ≤ 10^9). It then calculates either `a * n` or `b * k - k * (k - 1) / 2 + (n - k) * a`, where `k = min(n, b - a)`. Depending on whether `b <= a` or not, it prints the corresponding calculated value for each test case.

