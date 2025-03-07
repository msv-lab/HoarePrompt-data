#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, and for each test case, n, a, and b are integers where 1 <= n <= 100 and 1 <= a, b <= 30.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n % 2:
            if 2 * a < b:
                print(a * n)
            else:
                print(n // 2 * b + a)
        elif 2 * a < b:
            print(a * n)
        else:
            print(n // 2 * b)
        
    #State: The loop has completed all iterations, and the values of `n`, `a`, and `b` for each test case have been processed according to the conditions specified in the loop. The loop variable `_` is equal to `t - 1`, where `t` is the initial number of test cases. The conditions `1 <= n <= 100` and `1 <= a, b <= 30` remain true for each processed test case.
#Overall this is what the function does:The function processes a series of test cases, each defined by integers `n`, `a`, and `b` where `1 <= n <= 100` and `1 <= a, b <= 30`. For each test case, it calculates and prints a result based on the following logic: if `n` is odd and `2 * a < b`, it prints `a * n`; if `n` is odd and `2 * a >= b`, it prints `n // 2 * b + a`; if `n` is even and `2 * a < b`, it prints `a * n`; if `n` is even and `2 * a >= b`, it prints `n // 2 * b`. After processing all test cases, the function completes and the program state is such that all test cases have been processed and their respective results have been printed.

