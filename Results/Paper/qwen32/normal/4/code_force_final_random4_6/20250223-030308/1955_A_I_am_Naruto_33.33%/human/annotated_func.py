#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n, a, and b are integers such that 1 ≤ n ≤ 100, 1 ≤ a ≤ 30, and 1 ≤ b ≤ 30.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n > 1:
            ans1 = a * n
            ans2 = b * n // 2 + a * n % 2
            print(min(ans1, ans2))
        else:
            print(a)
        
    #State: `t` is the initial number of test cases, and `n`, `a`, `b` are the values from the last test case processed. `ans1` and `ans2` are not defined after the loop.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of three integers `n`, `a`, and `b`. For each test case, it calculates and prints a value based on the given conditions. Specifically, it computes two possible values: `ans1` as `a * n` and `ans2` as `b * n // 2 + a * n % 2` when `n` is greater than 1, and directly prints `a` when `n` is 1. The function prints the minimum of `ans1` and `ans2` for each test case.

