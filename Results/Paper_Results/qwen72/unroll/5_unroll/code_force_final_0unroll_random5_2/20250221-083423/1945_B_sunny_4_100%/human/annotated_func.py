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
        
    #State: After the loop executes all iterations, the values of `t`, `a`, `b`, and `m` remain unchanged, but the loop has printed the sum of `m // a + m // b + 2` for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by three integers `a`, `b`, and `m` (1 <= a, b, m <= 10^18). It reads the number of test cases `t` (1 <= t <= 10^4) from the input, and for each test case, it calculates the value `m // a + m // b + 2` and prints this result. After processing all test cases, the function does not return any value, but the input variables `t`, `a`, `b`, and `m` remain unchanged.

