#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, a, and b are integers such that 1 <= n <= 100, 1 <= a <= 30, and 1 <= b <= 30.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n > 1:
            ans1 = a * n
            ans2 = b * n // 2 + a * n % 2
            print(min(ans1, ans2))
        else:
            print(a)
        
    #State: `t` is 0, and for each of the initial `t` test cases, the output is either `a` (if `n` is 1) or the minimum of `a * n` and `b * n // 2 + a * n % 2` (if `n` is greater than 1).
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `n`, `a`, and `b`. For each test case, it computes and prints the minimum cost, where the cost is either `a * n` or `b * n // 2 + a * n % 2`, depending on the value of `n`. If `n` is 1, it simply prints `a`.

