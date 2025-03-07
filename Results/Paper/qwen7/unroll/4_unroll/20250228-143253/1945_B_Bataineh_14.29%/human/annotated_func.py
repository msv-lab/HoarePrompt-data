#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a or m < b:
            print(2)
        else:
            print(m // a + m // b + 2)
        
    #State: Output State: The output state will consist of `t` lines, each containing either 2 or a value calculated from the expression `m // a + m // b + 2`, depending on the input values for `a`, `b`, and `m` provided by the user for each iteration of the loop. Each line corresponds to one of the `t` iterations of the loop.
#Overall this is what the function does:The function processes up to 10,000 test cases. For each test case, it reads three integers \(a\), \(b\), and \(m\) (each between 1 and \(10^{18}\)). If \(m\) is less than both \(a\) and \(b\), it prints 2. Otherwise, it calculates and prints the value of \(\frac{m}{a} + \frac{m}{b} + 2\). After processing all test cases, it outputs a series of results, one per line, corresponding to each test case.

