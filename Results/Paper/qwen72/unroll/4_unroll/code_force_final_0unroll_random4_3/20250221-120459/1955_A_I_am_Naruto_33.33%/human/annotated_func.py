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
        
    #State: The loop has finished executing for all test cases. For each test case, if n > 1, the minimum value between `a * n` and `b * n // 2 + a * n % 2` is printed. If n == 1, the value of `a` is printed. The values of `t`, `n`, `a`, and `b` remain unchanged as they were in the initial state.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by integers `n`, `a`, and `b` within specified ranges. For each test case, if `n > 1`, it calculates two values: `a * n` and `b * n // 2 + a * n % 2`, and prints the minimum of these two values. If `n == 1`, it prints the value of `a`. The function does not modify the input values `t`, `n`, `a`, and `b`. After processing all test cases, the function concludes without returning any value.

