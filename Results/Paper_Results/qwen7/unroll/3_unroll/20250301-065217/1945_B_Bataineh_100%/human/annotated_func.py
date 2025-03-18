#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a and m < b:
            print(2)
        elif m < a and m > b:
            print(2 + m // b)
        elif m < b and m > a:
            print(2 + m // a)
        else:
            print(m // a + m // b + 2)
        
    #State: Output State: The output state will consist of a series of integers printed during each iteration of the loop, based on the conditions provided in the loop body. Each line of output corresponds to the result of processing one set of inputs (a, b, m) for a given value of `i` in the range of `t`. The exact values will depend on the specific inputs provided for each iteration.
#Overall this is what the function does:The function processes a series of test cases, each containing three integers \(a\), \(b\), and \(m\) (where \(1 \leq a, b, m \leq 10^{18}\)), and prints an integer result for each test case based on specific conditions. If \(m < a\) and \(m < b\), it prints 2. If \(m < a\) and \(m > b\), it prints \(2 + \frac{m}{b}\). If \(m < b\) and \(m > a\), it prints \(2 + \frac{m}{a}\). Otherwise, it prints \(\frac{m}{a} + \frac{m}{b} + 2\). The function reads the number of test cases \(t\) (where \(1 \leq t \leq 10^4\)) at the beginning and processes each test case individually.

