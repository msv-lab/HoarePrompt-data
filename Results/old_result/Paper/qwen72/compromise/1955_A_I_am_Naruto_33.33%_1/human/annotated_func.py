#State of the program right berfore the function call: t is an integer where 1 <= t <= 10^4, and for each test case, n, a, and b are integers such that 1 <= n <= 100 and 1 <= a, b <= 30.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n > 1:
            ans1 = a * n
            ans2 = b * n // 2 + a * n % 2
            print(min(ans1, ans2))
        else:
            print(a)
        
    #State: The loop has finished executing, and for each test case, the minimum value between `a * n` and `b * n // 2 + a * n % 2` has been printed. The variables `t`, `n`, `a`, and `b` retain their initial values, and no new variables are introduced.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case consists of integers `n`, `a`, and `b` with the constraints 1 <= n <= 100 and 1 <= a, b <= 30. For each test case, if `n` is greater than 1, the function calculates two values: `a * n` and `b * n // 2 + a * n % 2`, and prints the minimum of these two values. If `n` is 1, the function prints `a`. After processing all test cases, the function completes, and the variables `t`, `n`, `a`, and `b` retain their initial values.

