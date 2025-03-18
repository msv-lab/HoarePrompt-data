#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
def func():
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIRS')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: Output State: `t` is an integer such that \(1 \leq t \leq 1000\), `i` is \(t-1\), `a` is the first integer from the input, `b` is the second integer from the input, and `c` is the third integer from the input.
    #
    #After all iterations of the loop have finished, the variable `i` will be equal to `t-1` because the loop runs from `0` to `t-1`. The values of `a`, `b`, and `c` will be the integers from the last set of inputs provided, since these values are read in each iteration but not modified within the loop. The value of `t` remains unchanged throughout the loop's execution.
#Overall this is what the function does:The function processes up to 1000 test cases, where each test case consists of three integers \(a\), \(b\), and \(c\) (each between 0 and 9). For each test case, it prints 'STAIRS' if \(a < b < c\), 'PEAK' if \(a < b > c\), and 'NONE' otherwise. After processing all test cases, the function does not return any value but outputs the results directly.

