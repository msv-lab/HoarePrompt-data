#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    for i in range(int(input())):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 == 0 and b % 2 == 0:
            print('yes')
        elif (a - b == -a, a) or (b - a == -b, b):
            print('no')
        elif (a - b) % 2 > 0 or (a - b) % 2 < 0:
            print('yes')
        else:
            print('no')
        
    #State: After all iterations of the loop have finished, `t` is a positive integer such that \(1 \leq t \leq 10^4\), and for each test case, `a` and `b` are positive integers such that \(1 \leq a, b \leq 10^9\). The value of `i` will be equal to `t` since the loop runs `t` times. For each iteration, the program reads a line with two integers `a` and `b`, and prints either 'yes' or 'no' based on the given conditions. After all iterations, the output consists of `t` lines, each containing either 'yes' or 'no' depending on the inputs provided for each test case.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \(t\), \(a\), and \(b\), where \(1 \leq t \leq 10^4\) and \(1 \leq a, b \leq 10^9\). For each test case, it reads the values of \(a\) and \(b\), and prints 'yes' or 'no' based on specific conditions. After processing all test cases, it outputs a sequence of 'yes' or 'no' for each test case.

