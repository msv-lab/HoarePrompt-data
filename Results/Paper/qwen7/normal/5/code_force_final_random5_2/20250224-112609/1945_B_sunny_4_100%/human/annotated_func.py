#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^{18}.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ `t` ≤ 10^4, `qi` is 10000 (or the final value of `t` after all iterations), `a` is an input integer from one of the iterations, `b` is an input integer from one of the iterations, `m` is an input integer from one of the iterations, `ans` is the final value of `m // a + m // b + 2` calculated in the last iteration.
    #
    #In this final state, `qi` will have reached its maximum possible value of `t` (which is at most 10^4), and `a`, `b`, and `m` will hold the values from the last iteration of the loop. The variable `ans` will contain the result of the expression `m // a + m // b + 2` evaluated for the last set of inputs provided.
#Overall this is what the function does:The function processes up to 10,000 test cases. For each test case, it reads three integers \(a\), \(b\), and \(m\) and calculates the value of \( \text{m} // a + \text{m} // b + 2 \). It then prints this calculated value for each test case. After processing all test cases, the function does not return any value but prints the results for each test case.

