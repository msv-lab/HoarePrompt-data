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
        
    #State: The loop will execute n times, and for each iteration, it will read three integers a, b, and c from the input. It will then calculate d as c / 2. If a * b is less than a * d, it will print a * b; otherwise, it will print the rounded value of a * d. The values of t and n remain unchanged, and the values of a, b, and c are read from input during each iteration and are not retained between iterations.
#Overall this is what the function does:The function `func` reads an integer `n` from the input, which represents the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` from the input. It calculates `d` as `c / 2`. If `a * b` is less than `a * d`, it prints `a * b`; otherwise, it prints the rounded value of `a * d`. The function does not return any value; it only prints the results of the calculations for each test case. The values of `t` and `n` remain unchanged, and the values of `a`, `b`, and `c` are read from the input during each iteration and are not retained between iterations.

