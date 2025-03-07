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
        
    #State: Output State: The value of `z` after all iterations of the loop have finished, based on the input values provided within the loop. Specifically, for each iteration `i` in the range of `a`, the value of `z` is calculated based on the inputs `x` and `y`, and then updated if necessary according to the conditions in the loop. The final value of `z` after all iterations will be printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two non-negative integers \(x\) and \(y\) (both between 0 and 99), and a positive integer \(t\) (between 1 and \(10^4\)). For each test case, it calculates a value \(z\) based on \(x\), \(y\), and \(t\), and updates \(z\) if necessary according to specific conditions. After processing all test cases, it prints the final value of \(z\) for each case.

