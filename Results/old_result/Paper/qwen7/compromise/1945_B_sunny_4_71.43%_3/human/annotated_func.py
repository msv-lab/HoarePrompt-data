#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: Output State: The sum of (int(m/a) + 1) and (int(m/b) + 1) for each iteration, where `a`, `b`, and `m` are integers provided as input for each iteration, and `t` is the number of iterations.
#Overall this is what the function does:The function processes a series of test cases, each defined by integers \(a\), \(b\), and \(m\). For each test case, it calculates the sum of \(\left\lfloor \frac{m}{a} \right\rfloor + 1\) and \(\left\lfloor \frac{m}{b} \right\rfloor + 1\), and prints the result. The function reads the number of test cases \(t\) from the input first, where \(1 \leq t \leq 10^4\), and then processes each test case accordingly. After processing all test cases, it outputs the calculated sums for each case.

