#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three integers a, b, m such that 1 ≤ a, b, m ≤ 10^{18}.
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
        
    #State: Output State: t test cases are processed, and for each test case, the value of `ans` (calculated as `m // a + m // b + 2`) is printed. The total number of test cases is equal to the initial value of `t`.
#Overall this is what the function does:The function processes up to 10,000 test cases, where each test case consists of three integers \(a\), \(b\), and \(m\) (with \(1 \leq a, b, m \leq 10^{18}\)). For each test case, it calculates the value of \(ans\) as \(\left\lfloor \frac{m}{a} \right\rfloor + \left\lfloor \frac{m}{b} \right\rfloor + 2\) and prints the result. After processing all test cases, it outputs the calculated value for each case.

