#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^18.
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
        
    #State: The loop has executed `t` times, where `t` is the initial input integer such that 1 ≤ `t` ≤ 10^4. For each of the `t` iterations, the values of `a`, `b`, and `m` were read from the input. The value of `ans` was calculated as `m // a + m // b + 2` and printed. The variable `qi` has taken on each integer value from 0 to `t-1` during the loop's execution.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `m`. It calculates and prints the value of `m // a + m // b + 2`.

