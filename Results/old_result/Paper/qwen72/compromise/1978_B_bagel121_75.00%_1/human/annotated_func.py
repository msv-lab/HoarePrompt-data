#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, and for each test case, n, a, and b are integers where 1 ≤ n, a, b ≤ 10^9.
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
        
    #State: The loop has finished executing all iterations. For each test case, the output is either `n * a` if `a >= b`, or the sum of `int((b + (b - k + 1)) / 2 * k)` and `(n - k) * a` if `a < b`, where `k` is the minimum of `b - a + 1` and `n`. The values of `t`, `n`, `a`, and `b` remain unchanged as they are input for each test case.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases, where 1 ≤ t ≤ 10^4. For each test case, it reads three integers `n`, `a`, and `b` (1 ≤ n, a, b ≤ 10^9). If `a` is greater than or equal to `b`, the function prints `n * a`. Otherwise, it calculates `k` as the minimum of `b - a + 1` and `n`, computes `ans` as the integer value of `(b + (b - k + 1)) / 2 * k`, and `p2` as `(n - k) * a`, then prints the sum of `ans` and `p2`. After processing all test cases, the function concludes, and the values of `t`, `n`, `a`, and `b` remain unchanged as they are input for each test case.

