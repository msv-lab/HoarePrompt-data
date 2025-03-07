#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each of the following t lines contains three integers a, b, and m, where 1 ≤ a, b, m ≤ 10^18.
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
        
    #State: `t` is the same as the initial input integer, and `a`, `b`, and `m` are the values from the last test case processed.
#Overall this is what the function does:The function reads a positive integer `t` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `m`, and prints the result of `m // a + m // b + 2`.

