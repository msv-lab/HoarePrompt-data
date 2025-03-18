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
        
    #State: The value of `t` remains unchanged, and `n` is the number of iterations the loop has executed. For each iteration, the loop takes three integers `a`, `b`, and `c` as input, calculates `d` as `c / 2`, and prints either `a * b` or `round(a * d)` depending on the condition `a * b < a * d`. The values of `a`, `b`, and `c` are updated with each input, but their final values after the loop are the ones from the last iteration.
#Overall this is what the function does:The function `func` processes a series of test cases. It first reads an integer `n` from the input, which specifies the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` from the input. It then calculates `d` as `c / 2` and prints either `a * b` or `round(a * d)`, depending on whether `a * b` is less than `a * d`. After processing all test cases, the function has no return value, but it has printed the results of the calculations for each test case. The state of the program after the function concludes includes the value of `n` being the number of test cases processed, and the values of `a`, `b`, and `c` being those from the last test case. The value of `t` (if it exists in the calling context) remains unchanged.

