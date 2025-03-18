#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, n, a, and b are integers such that 1 <= n <= 100 and 1 <= a, b <= 30.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n > 1:
            ans1 = a * n
            ans2 = b * n // 2 + a * n % 2
            print(min(ans1, ans2))
        else:
            print(a)
        
    #State: `t` is an integer such that 1 <= t <= 10^4. For each of the `t` test cases, `n`, `a`, and `b` are assigned the values from the input, where `1 <= n <= 100` and `1 <= a, b <= 30`. If `n` > 1, `ans1` is equal to `a * n`, and `ans2` is equal to `b * n // 2 + a * n % 2`. The minimum of `ans1` and `ans2` is printed. If `n` is less than or equal to 1, `a` is printed.
#Overall this is what the function does:The function processes a series of test cases, each defined by three integers `n`, `a`, and `b` where `1 <= n <= 100` and `1 <= a, b <= 30`. For each test case, if `n` is greater than 1, it calculates two values: `ans1` as `a * n` and `ans2` as `b * n // 2 + a * n % 2`, and prints the minimum of these two values. If `n` is 1 or less, it prints `a`. The function does not return any value; it only prints the results for each test case.

