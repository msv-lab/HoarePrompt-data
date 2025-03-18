#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each of the t test cases, n, a, and b are integers such that 1 <= n <= 100 and 1 <= a, b <= 30.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n > 1:
            ans1 = a * n
            ans2 = b * n // 2 + a * n % 2
            print(min(ans1, ans2))
        else:
            print(a)
        
    #State: After processing all t test cases, the program will have printed the minimum cost for each test case based on the given formulae. The variables t, n, a, b, ans1, and ans2 will no longer hold their initial values as they are updated in each iteration of the loop. The state of other variables not mentioned in the loop remains unchanged.
#Overall this is what the function does:The function processes a series of test cases, each defined by three integers `n`, `a`, and `b`. For each test case, it calculates and prints the minimum cost based on the given criteria. The cost is determined by either `a * n` or `b * n // 2 + a * n % 2`, whichever is smaller, unless `n` is 1, in which case the cost is simply `a`. After processing all test cases, the function outputs the calculated minimum cost for each one.

