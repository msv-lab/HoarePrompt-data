#State of the program right berfore the function call: Each test case consists of three integers n, a, and b, where 1 ≤ n, a, b ≤ 10^9. There are t test cases, where 1 ≤ t ≤ 10^4.
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
        
    #State: The loop has executed `t` times, with `t` being the number of test cases. For each test case, the program reads integers `n`, `a`, and `b`. If `a` is greater than or equal to `b`, it prints `n * a`. Otherwise, it calculates `k` as the minimum of `b - a + 1` and `n`, computes `ans` as `int((b + (b - k + 1)) / 2 * k)`, and `p2` as `(n - k) * a`, then prints `ans + p2`. After all iterations, `t` test cases have been processed and their respective results printed.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `n`, `a`, and `b`. For each test case, it calculates and prints a result based on the values of `n`, `a`, and `b`. If `a` is greater than or equal to `b`, it prints `n * a`. Otherwise, it calculates a sum involving the minimum of `b - a + 1` and `n`, and prints the sum of this calculated value and `(n - k) * a`. After processing all test cases, it outputs the result for each.

