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
        
    #State: The values of t, n, a, and b remain unchanged. For each iteration of the loop, the output will be either a * b or round(a * d), depending on the condition a * b < a * d. The variable c is read from input and used to calculate d, but its value is not stored or used outside the loop.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads three integers `a`, `b`, and `c` from the input, where `1 <= a, b <= 30` and `c` is any integer. It calculates `d` as `c / 2` and then prints either `a * b` or `round(a * d)`, depending on whether `a * b` is less than `a * d`. The function does not return any value; it only prints the results for each test case. The values of `t`, `n`, `a`, and `b` remain unchanged throughout the function's execution, and `c` is not stored or used outside the loop.

