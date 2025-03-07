#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and for each test case, n, a, and b are positive integers such that 1 ≤ n, a, b ≤ 10^9.
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
        
    #State: Output State: The output state will consist of multiple lines, where each line corresponds to the output of one test case. For each test case, if `a >= b`, it will print `n * a`. Otherwise, it calculates and prints `ans + p2` based on the given formulae, where `k` is the minimum of `b - a + 1` and `n`, `ans` is the sum of an arithmetic series, and `p2` is the sum of `a` repeated for `n - k` times.
#Overall this is what the function does:The function processes `t` test cases, where for each test case, it accepts three positive integers `n`, `a`, and `b` such that 1 ≤ n, a, b ≤ 10^9. If `a` is greater than or equal to `b`, it prints `n * a`. Otherwise, it calculates and prints `ans + p2`, where `k` is the minimum of `b - a + 1` and `n`, `ans` is the sum of an arithmetic series, and `p2` is the sum of `a` repeated for `n - k` times. After processing all test cases, it outputs the results for each test case.

