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
        
    #State: The loop has finished executing all iterations, and for each test case, the output is the minimum value between `a * n` and `b * n // 2 + a * n % 2` if `n > 1`, or simply `a` if `n == 1`. The values of `t`, `n`, `a`, and `b` remain unchanged as they were provided in the input.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by integers `n`, `a`, and `b` where 1 <= n <= 100 and 1 <= a, b <= 30. For each test case, if `n > 1`, it calculates the minimum value between `a * n` and `b * n // 2 + a * n % 2` and prints this minimum value. If `n == 1`, it simply prints `a`. After processing all test cases, the function completes, and the values of `t`, `n`, `a`, and `b` remain unchanged as they were provided in the input.

