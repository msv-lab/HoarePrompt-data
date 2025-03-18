#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n > 1:
            ans1 = a * n
            ans2 = b * n // 2 + a * n % 2
            print(min(ans1, ans2))
        else:
            print(a)
        
    #State: t is an integer such that 0 ≤ t ≤ 10^4 - t_initial, where t_initial is the initial value of t; no more iterations will occur as t has reached 0.
#Overall this is what the function does:The function processes a number of test cases, each defined by three integers `n`, `a`, and `b`. For each test case, it calculates and prints the minimum cost, where the cost is determined by either `a * n` or `b * (n // 2) + a * (n % 2)`, depending on the value of `n`. If `n` is 1, it simply prints `a`.

