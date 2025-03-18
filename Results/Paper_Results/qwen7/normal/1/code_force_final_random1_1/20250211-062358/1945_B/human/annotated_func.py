#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        mn = min(a, b) + m
        
        if m % a == 0 and m % b == 0 and a != 1 and b != 1:
            print(mn // a + mn // b + 1)
        else:
            print(mn // a + mn // b)
        
    #State: Output State: `t` must be greater than 0, `i` is equal to `t`, `a` is an input integer, `b` is an input integer, `m` is an input integer, `mn` is the minimum of `a` and `b` plus `m`. After all iterations, the value of `i` will be equal to the initial value of `t`, as the loop increments `i` from 0 to `t-1`. The values of `a`, `b`, `m`, and `mn` will be updated based on each iteration's input but will not retain their values across iterations. No specific values can be determined for `a`, `b`, `m`, and `mn` without knowing the inputs, but they will reflect the last processed input within the loop.
#Overall this is what the function does:The function processes up to 10,000 test cases, each consisting of three integers \(a\), \(b\), and \(m\) (where \(1 \leq a, b, m \leq 10^{18}\)). For each test case, it calculates a value based on the minimum of \(a\) and \(b\) plus \(m\), and prints either \(\frac{mn}{a} + \frac{mn}{b} + 1\) or \(\frac{mn}{a} + \frac{mn}{b}\) depending on whether \(m\) is divisible by both \(a\) and \(b\) and neither \(a\) nor \(b\) is 1. After processing all test cases, it outputs the calculated value for each case.

