#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, a, b, and m are integers such that 1 <= a, b, m <= 10^18.
def func():
    """t=int(input())
    for _ in range(t):
        a,b,m=map(int,input().split())
        A=int(m/a)+1
        B=int(m/b)+1
        print(A+B)"""
    t = int(input())
    for qi in range(t):
        a, b, m = [int(x) for x in input().split()]
        
        ans = m // a + m // b + 2
        
        print(ans)
        
    #State: The loop executes `t` times, and for each iteration, it reads three integers `a`, `b`, and `m` from the input. It then calculates `ans` as `m // a + m // b + 2` and prints `ans`. After all iterations, the values of `t`, `a`, `b`, and `m` remain unchanged, but the output consists of `t` lines, each containing the value of `ans` for the corresponding test case.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each of the `t` test cases, it reads three integers `a`, `b`, and `m` from the input. It then calculates the value `ans` as `m // a + m // b + 2` and prints `ans`. After processing all test cases, the function does not return any value, but the output consists of `t` lines, each containing the calculated value of `ans` for the corresponding test case. The values of `t`, `a`, `b`, and `m` are not modified by the function.

