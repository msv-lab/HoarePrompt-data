#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, and for each test case, a, b, and m are positive integers such that 1 <= a, b, m <= 10^18.
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
        
    #State: `t` must be greater than or equal to the initial value of `t`, `qi` is `t-1`, `a`, `b`, and `m` are input integers, `ans` is equal to `m // a + m // b + 2`.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `m` from the input. It then calculates the value `ans` as `m // a + m // b + 2` and prints this value. After processing all test cases, the function does not return any value, but the state of the program includes `t` being equal to the initial number of test cases, `qi` being `t-1`, and `a`, `b`, and `m` being the last set of input integers for the final test case.

