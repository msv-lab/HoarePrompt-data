#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three integers a, b, and m, where 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        mn = min(a, b) + m
        
        if m % a == 0 and m % b == 0 and a != 1 and b != 1:
            print(mn // a + mn // b + 1)
        else:
            print(mn // a + mn // b)
        
    #State: Output State: The output state will consist of `t` lines, each containing either `(mn // a + mn // b + 1)` or `(mn // a + mn // b)`, depending on the conditions specified in the loop body. Here, `mn` is calculated as `min(a, b) + m`, where `a`, `b`, and `m` are integers provided by user input for each iteration of the loop.
#Overall this is what the function does:The function processes up to 10,000 test cases, each consisting of three integers \(a\), \(b\), and \(m\) (all between 1 and \(10^{18}\)). For each test case, it calculates a value \(mn\) as the minimum of \(a\) and \(b\) plus \(m\). Depending on whether \(m\) is divisible by both \(a\) and \(b\) and neither \(a\) nor \(b\) is 1, it prints either \(\frac{mn}{a} + \frac{mn}{b} + 1\) or \(\frac{mn}{a} + \frac{mn}{b}\). The function outputs these results for all test cases.

