#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three integers a, b, and m, where 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a or m < b:
            print(2)
        else:
            print(m // a + m // b + 2)
        
    #State: After the loop executes all iterations, `i` will be equal to `t-1`, `a`, `b`, and `m` will be updated to the values entered by the user for each iteration of the loop.
#Overall this is what the function does:The function processes up to 10,000 test cases, each consisting of three integers \(a\), \(b\), and \(m\). For each test case, it calculates and prints either 2 or the value of \(\left\lfloor \frac{m}{a} \right\rfloor + \left\lfloor \frac{m}{b} \right\rfloor + 2\) based on whether \(m\) is less than both \(a\) and \(b\).

