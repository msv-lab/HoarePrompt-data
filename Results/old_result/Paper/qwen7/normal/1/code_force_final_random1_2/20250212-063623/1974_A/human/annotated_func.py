#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, x and y are non-negative integers such that 0 ≤ x, y ≤ 99.
def func():
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        
        z = (y + 1) // 2
        
        m = 15 * z - y * 4
        
        if m < a:
            z = z + (x - m + 15 - 1) // 15
        
        print(z)
        
    #State: After all iterations of the loop, `t` is a positive integer such that 1 ≤ t ≤ 10^4, `a` is an input integer, `i` is equal to `a`, `x` is the first integer entered, `y` is the second integer entered, `z` is \((y + 1) // 2 + (x - m + 14) // 15\), and `m` is \(15 * ((y + 1) // 2) - y * 4\). If `m` is less than `a` during any iteration, `z` is updated to \((y + 1) // 2 + (x - m + 14) // 15\). The final value of `z` will be the maximum value of `z` calculated during any iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two non-negative integers \(x\) and \(y\). For each test case, it calculates a value \(z\) based on \(x\) and \(y\). Specifically, \(z\) is initially set to \((y + 1) // 2\), then adjusted if necessary based on \(x\) and another calculated value \(m\). The final value of \(z\) for each test case is the maximum value of \(z\) calculated during the process. The function does not return any value but prints the final calculated \(z\) for each test case.

