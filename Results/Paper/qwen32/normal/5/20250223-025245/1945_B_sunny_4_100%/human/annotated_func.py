#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each of the following t lines contains three integers a, b, and m such that 1 ≤ a, b, m ≤ 10^18.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `a`, `b`, and `m` are integers read from input; `ans` is `m // a + m // b + 2` for each of the `t` iterations; `qi` is `t-1`
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of three integers `a`, `b`, and `m`. For each test case, it calculates the value of `m // a + m // b + 2` and prints the result.

