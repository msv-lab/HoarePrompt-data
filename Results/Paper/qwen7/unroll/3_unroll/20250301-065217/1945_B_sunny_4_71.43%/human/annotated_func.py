#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: Output State: The sum of \(A + B\) for each iteration of the loop, where \(A = \left\lfloor \frac{m}{a} \right\rfloor + 1\) and \(B = \left\lfloor \frac{m}{b} \right\rfloor + 1\), for all given pairs of \(a\), \(b\), and \(m\).
#Overall this is what the function does:The function processes up to 10,000 test cases, each consisting of three integers \(a\), \(b\), and \(m\). For each test case, it calculates \(A\) as \(\left\lfloor \frac{m}{a} \right\rfloor + 1\) and \(B\) as \(\left\lfloor \frac{m}{b} \right\rfloor + 1\), then prints the sum \(A + B\). After processing all test cases, it outputs the sum for each case.

