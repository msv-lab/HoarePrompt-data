#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, n, a, and b are integers such that 1 <= n <= 100 and 1 <= a, b <= 30.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        d = c / 2
        
        if a * b < a * d:
            print(a * b)
        else:
            print(round(a * d))
        
    #State: The loop iterates n times, and for each iteration, it reads three integers a, b, and c from the input. It then calculates d as c divided by 2. If the product of a and b is less than the product of a and d, it prints a * b. Otherwise, it prints the rounded value of a * d. The values of t and n remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `n` from the input, and for each of the `n` iterations, it reads three integers `a`, `b`, and `c` from the input. It calculates `d` as `c` divided by 2. If the product of `a` and `b` is less than the product of `a` and `d`, it prints `a * b`. Otherwise, it prints the rounded value of `a * d`. The function does not return any value. The values of `t` and `n` remain unchanged after the function concludes.

