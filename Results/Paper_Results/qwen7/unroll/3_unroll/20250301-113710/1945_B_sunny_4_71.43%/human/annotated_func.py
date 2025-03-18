#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three integers a, b, and m, where 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: Output State: The sum of \(A + B\) for each iteration, where \(A = \left\lceil \frac{m}{a} \right\rceil + 1\) and \(B = \left\lceil \frac{m}{b} \right\rceil + 1\), for all \(t\) test cases.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \(a\), \(b\), and \(m\). For each test case, it calculates the values of \(A\) and \(B\) using the formulas \(A = \left\lceil \frac{m}{a} \right\rceil + 1\) and \(B = \left\lceil \frac{m}{b} \right\rceil + 1\), and then prints the sum \(A + B\). After processing all test cases, it outputs the sum for each case.

