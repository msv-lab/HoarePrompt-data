#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, n, a, and b are integers such that 1 <= n <= 100 and 1 <= a, b <= 30.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        s1 = n * a
        
        s2 = b * (n // 2) + n % 2 * a
        
        print(min(s1, s2))
        
    #State: `t` is an integer such that 1 <= t <= 10^4, and for each test case, `n`, `a`, and `b` have been processed, with `s1` calculated as `n * a` and `s2` calculated as `b * (n // 2) + n % 2 * a`. The minimum of `s1` and `s2` has been printed for each test case. The loop has completed all its iterations based on the input value of `t`.
#Overall this is what the function does:The function processes a series of test cases defined by an integer `t` (1 <= t <= 10^4). For each test case, it reads three integers `n`, `a`, and `b` (1 <= n <= 100, 1 <= a, b <= 30). It calculates two values: `s1` as `n * a` and `s2` as `b * (n // 2) + n % 2 * a`. The function then prints the minimum of `s1` and `s2` for each test case. After processing all test cases, the function completes without returning any value.

