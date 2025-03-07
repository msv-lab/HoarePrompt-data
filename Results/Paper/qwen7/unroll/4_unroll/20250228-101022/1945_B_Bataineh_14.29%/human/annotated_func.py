#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a or m < b:
            print(2)
        else:
            print(m // a + m // b + 2)
        
    #State: Output State: The output state will consist of a series of integers printed during each iteration of the loop. For each iteration, the program reads three integers \(a\), \(b\), and \(m\) from the input. If \(m\) is less than either \(a\) or \(b\), it prints 2. Otherwise, it prints the result of \(\frac{m}{a} + \frac{m}{b} + 2\). The total output state will be a list of these printed integers, one for each iteration of the loop.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \(t\), \(a\), and \(m\). For each test case, it reads the values of \(a\), \(b\), and \(m\) from the input. If \(m\) is less than either \(a\) or \(b\), it prints 2. Otherwise, it prints the value of \(\frac{m}{a} + \frac{m}{b} + 2\). After processing all test cases, it outputs a list of these printed integers, one for each test case.

