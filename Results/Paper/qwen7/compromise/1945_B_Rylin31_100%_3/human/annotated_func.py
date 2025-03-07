#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three integers a, b, and m, where 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        print(m // a + m // b + 2)
        
    #State: Output State: The output state will consist of `t` lines, where each line contains the result of the expression `m // a + m // b + 2` for the corresponding input values of `a`, `b`, and `m` provided in the `t` iterations of the loop. Each input set `(a, b, m)` is processed independently, and the results are printed in sequence.
#Overall this is what the function does:The function processes up to 10,000 test cases, each consisting of three integers \(a\), \(b\), and \(m\). For each test case, it calculates the value of \(\frac{m}{a} + \frac{m}{b} + 2\) and prints the result. The function does not return any value but prints the calculated results for each test case.

