#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, a, and b are integers such that 1 <= n <= 100 and 1 <= a, b <= 30.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        d = c / 2
        
        if a * b < a * d:
            print(a * b)
        else:
            print(round(a * d))
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is an input integer, where 1 <= `n` <= 100; `a` and `b` are integers such that 1 <= `a`, `b` <= 30.
#Overall this is what the function does:The function reads multiple test cases, each consisting of three integers `a`, `b`, and `c`. For each test case, it calculates and prints the result of either `a * b` or the rounded value of `a * (c / 2)`, whichever is smaller.

