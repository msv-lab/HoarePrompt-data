#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and each test case consists of three positive integers n, a, and b such that 1 ≤ n, a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if a >= b:
            print(n * a)
        else:
            k = min(b - a + 1, n)
            ans = int((b + (b - k + 1)) / 2 * k)
            p2 = (n - k) * a
            print(ans + p2)
        
    #State: t must be a positive integer, n is an input integer, a is an input integer, b is an input integer, k is the minimum value between b - a + 1 and n, ans is the integer value of \(\frac{(b + (b - k + 1))}{2} \times k\), p2 is \((n - k) \times a\).
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of three positive integers `n`, `a`, and `b`. For each test case, it calculates and prints a result based on the values of `n`, `a`, and `b`. If `a` is greater than or equal to `b`, it prints `n * a`. Otherwise, it calculates and prints a value derived from `n`, `a`, and `b` using specific formulas.

