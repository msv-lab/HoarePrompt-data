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
        
    #State: `t` is an input integer such that 1 <= t <= 10^4, `a`, `b`, and `m` are integers such that 1 <= a, b, m <= 10^18, `A` is `int(m/a) + 1`, and `B` is `int(m/b) + 1`. The loop has printed `t` lines, each containing the value of `m // a + m // b + 2` for the corresponding input values of `a`, `b`, and `m`.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 10^4`, representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `m` from the input, where `1 <= a, b, m <= 10^18`. It then calculates the value `m // a + m // b + 2` and prints this value. After processing all `t` test cases, the function has printed `t` lines, each containing the calculated value for the corresponding test case. The function does not return any value.

