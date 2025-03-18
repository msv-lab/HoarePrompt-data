#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^{18}.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `A` is undefined, `B` is undefined
    #
    #Explanation: The provided code reads multiple test cases from standard input, where each test case consists of three integers `a`, `b`, and `m`. For each test case, it calculates `ans = m // a + m // b + 2` and prints the result. However, since the initial state does not provide any specific values for `A` and `B`, and these variables are not used within the loop, their values remain undefined after the loop completes. The value of `t` remains the same as the initial value, as the loop only processes `t` test cases but does not modify `t` itself.
#Overall this is what the function does:The function processes up to 10,000 test cases, where each test case consists of three integers \(a\), \(b\), and \(m\) (with \(1 \leq a, b, m \leq 10^{18}\)). For each test case, it calculates the value of \(ans = \left\lfloor \frac{m}{a} \right\rfloor + \left\lfloor \frac{m}{b} \right\rfloor + 2\) and prints the result. After processing all test cases, the function does not return any value but outputs the calculated results for each test case.

