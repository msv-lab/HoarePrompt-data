#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, there are three integers n, a, and b where 1 <= n <= 100 and 1 <= a, b <= 30.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        d = c / 2
        
        if a * b < a * d:
            print(a * b)
        else:
            print(round(a * d))
        
    #State: The loop has processed all `t` test cases. For each test case, it has performed `n` iterations, reading three integers `a`, `b`, and `c` in each iteration, calculating `d` as `c / 2`, and printing either `a * b` or `round(a * d)` based on the condition `a * b < a * d`. The values of `t`, `n`, `a`, `b`, and `c` are not retained after the loop finishes processing each test case.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `n`, `a`, and `b`, calculates `d` as `c / 2`, and prints either `a * b` or `round(a * d)` based on the condition `a * b < a * d`. The function processes each test case independently and outputs a result for each one.

