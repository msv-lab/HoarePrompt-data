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
        
    #State: Output State: t test cases have been processed, for each test case, the value of `ans` (calculated as `m // a + m // b + 2`) has been printed based on the input values of `a`, `b`, and `m`.
#Overall this is what the function does:The function processes up to 10,000 test cases. For each test case, it reads three integers \(a\), \(b\), and \(m\) (where \(1 \leq a, b, m \leq 10^{18}\)), calculates the value of \(ans\) as \(\left\lfloor \frac{m}{a} \right\rfloor + \left\lfloor \frac{m}{b} \right\rfloor + 2\), and prints the result. After processing all test cases, it outputs the calculated values for each case.

