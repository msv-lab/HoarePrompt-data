#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three integers a, b, and m, where 1 ≤ a, b, m ≤ 10^{18}.
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
        
    #State: Output State: `t` is an integer such that \(1 \leq t \leq 10^4\), `qi` is \(t-1\) (the total number of iterations minus one), `a` is the first integer input, `b` is the second integer input, `m` is the third integer input, `ans` is `m // a + m // b + 2`.
    #
    #This means that after all the iterations of the loop have finished, `qi` will be equal to \(t-1\), indicating that the loop has executed \(t\) times. The values of `a`, `b`, and `m` will be the same as the last inputs provided, and `ans` will be the result of the last calculation performed within the loop, which is `m // a + m // b + 2`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \(a\), \(b\), and \(m\). For each test case, it calculates the value of \(ans\) as \(m // a + m // b + 2\) and prints the result. After processing all test cases, the function outputs the calculated \(ans\) values for each case.

