#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        mn = min(a, b) + m
        
        if m % a == 0 and m % b == 0 and a != 1 and b != 1:
            print(mn // a + mn // b + 1)
        else:
            print(mn // a + mn // b)
        
    #State: Output State: The value of `t` is an integer between 1 and \(10^4\), `i` is equal to \(t-1\), `a`, `b`, and `m` are the last set of integers that were input during the loop's final iteration, and `mn` is the sum of `min(a, b)` and `m`. If `m` is divisible by both `a` and `b` and neither `a` nor `b` is 1, the output will be `mn // a + mn // b + 1`. Otherwise, the output will be `mn // a + mn // b`.
    #
    #This means that after all iterations of the loop have finished, the loop has processed all `t` inputs, and the final values of `a`, `b`, and `m` are those provided in the last input. The variable `i` will be `t-1` because the loop increments `i` from 0 to `t-1`.
#Overall this is what the function does:The function processes up to 10,000 test cases, where for each test case, it takes three integers \(a\), \(b\), and \(m\) (each between 1 and \(10^{18}\)). It calculates the minimum of \(a\) and \(b\) plus \(m\) and then computes either \(\frac{mn}{a} + \frac{mn}{b} + 1\) or \(\frac{mn}{a} + \frac{mn}{b}\) depending on whether \(m\) is divisible by both \(a\) and \(b\) and neither \(a\) nor \(b\) is 1. The function outputs these calculated values for each test case. After processing all test cases, it returns no value explicitly but ensures all inputs are processed and the corresponding calculations are performed.

