#State of the program right berfore the function call: Each test case consists of three integers a, b, and m (1 ≤ a, b, m ≤ 10^18), where a is the frequency of launching fireworks for the first installation, b is the frequency of launching fireworks for the second installation, and m is the time each firework is visible in the sky. There are t (1 ≤ t ≤ 10^4) test cases.
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
        
    #State: Each test case has been processed, `t` is an input integer, `a`, `b`, and `m` hold the values from the last test case, and `ans` holds the result of the last iteration (`m // a + m // b + 2`).
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers `a`, `b`, and `m`. For each test case, it calculates and prints the number of time intervals during which fireworks from both installations are visible in the sky simultaneously.

