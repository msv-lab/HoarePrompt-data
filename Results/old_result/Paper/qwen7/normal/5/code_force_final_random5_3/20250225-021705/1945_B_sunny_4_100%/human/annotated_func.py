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
        
    #State: Output State: `t` is greater than 0 and less than or equal to 10^4, `qi` is equal to `t`, `a` is an input integer, `b` is an input integer, `m` is an input integer, `ans` is `m // a + m // b + 2` for each iteration from 0 to `t-1`.
    #
    #This means that after the loop has executed all its iterations, `t` will still be within the range of 1 to 10^4 (inclusive), `qi` will have the value of `t` since it increments by 1 in each iteration of the loop, and `a`, `b`, and `m` will hold the last values provided as input for the final iteration of the loop. The variable `ans` will contain the result of the expression `m // a + m // b + 2` for the last set of inputs processed.
#Overall this is what the function does:The function processes up to 10,000 test cases, where for each test case, it takes three integers \(a\), \(b\), and \(m\) as input. For each set of inputs, it calculates the value of \( \text{ans} = \left\lfloor \frac{m}{a} \right\rfloor + \left\lfloor \frac{m}{b} \right\rfloor + 2 \) and prints the result. After processing all test cases, the function outputs the calculated values for each test case.

