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
        
    #State: t is an input integer between 1 and 10^4, and for each test case, a, b, and m are integers such that 1 <= a, b, m <= 10^18. A is int(m/a) + 1, B is int(m/b) + 1, and A + B is printed for each test case. The loop has finished executing, and the values of a, b, and m are unchanged for each test case.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 10^4`, representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `m` from the input, where `1 <= a, b, m <= 10^18`. It then calculates the value `ans` as `m // a + m // b + 2` and prints this value. After processing all test cases, the function completes, and the values of `a`, `b`, and `m` are reset for each new test case. The function does not return any value; it only prints the results.

