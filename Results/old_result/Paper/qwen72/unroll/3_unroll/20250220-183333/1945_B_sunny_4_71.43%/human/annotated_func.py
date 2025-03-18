#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, a, b, and m are integers such that 1 <= a, b, m <= 10^18.
def func():
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: For each test case, the loop prints the value of \(A + B\), where \(A = \left\lfloor \frac{m}{a} \right\rfloor + 1\) and \(B = \left\lfloor \frac{m}{b} \right\rfloor + 1\). After all iterations, the values of \(t\), \(a\), \(b\), and \(m\) remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `m` from the input. It then calculates and prints the sum of two values: \(A = \left\lfloor \frac{m}{a} \right\rfloor + 1\) and \(B = \left\lfloor \frac{m}{b} \right\rfloor + 1\). After processing all test cases, the function does not return any value, but the values of `t`, `a`, `b`, and `m` remain unchanged.

