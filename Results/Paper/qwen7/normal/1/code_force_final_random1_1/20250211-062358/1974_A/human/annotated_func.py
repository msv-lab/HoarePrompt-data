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
        
    #State: After all iterations of the loop have finished, `i` will be equal to `a-1`, `x` and `y` will be the last input integers provided during the loop's execution, `z` will be the final calculated value based on the last iteration's `y` and `x`, and `m` will be the result of `15 * z - y * 4`. If the condition `m < a` was met during the last iteration, `z` will be adjusted accordingly.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads two integers \(x\) and \(y\), calculates a value \(z\) based on these inputs and an adjustment factor, and prints the final value of \(z\). The function iterates through all test cases and adjusts \(z\) if necessary based on the comparison between \(m\) and \(a\). After processing all test cases, the function does not return any value.

