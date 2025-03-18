#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, x and y are integers such that 0 ≤ x, y ≤ 99.
def func():
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        
        z = (y + 1) // 2
        
        m = 15 * z - y * 4
        
        if m < a:
            z = z + (x - m + 15 - 1) // 15
        
        print(z)
        
    #State: After all iterations of the loop, `t` is an integer such that \(1 \leq t \leq 10^4\), `a` is an input integer, `i` is equal to `a`, `x` is an input integer, `y` is an input integer, `z` is \((y + 1) // 2 + (x - m + 14) // 15\) if `m < a`, or \((y + 1) // 2\) otherwise, where `m` is \(15 \cdot ((y + 1) // 2) - y \cdot 4\).
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \(x\) and \(y\) (where \(0 \leq x, y \leq 99\)), and an integer \(t\) (where \(1 \leq t \leq 10^4\)). For each test case, it calculates an integer \(z\) based on the values of \(x\) and \(y\), and prints the result. If \(m < a\) (where \(a\) is the number of test cases and \(m = 15 \cdot ((y + 1) // 2) - y \cdot 4\)), then \(z\) is adjusted by adding \((x - m + 15 - 1) // 15\) to \((y + 1) // 2\). Otherwise, \(z\) remains \((y + 1) // 2\). The function does not return any value.

