#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: `t` is a positive integer such that \(1 \leq t \leq 10^4\), `_` is \(t-1\), `a` and `b` are integers from the input, and if either `a` or `b` is even, they remain unchanged. If both `a` and `b` are odd, they remain unchanged as well.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer \(t\) (1 ≤ \(t\) ≤ 10^4) followed by two positive integers \(a\) and \(b\) (1 ≤ \(a\), \(b\) ≤ 10^9). For each test case, it checks if either \(a\) or \(b\) is even. If at least one of them is even, it prints 'Yes'; otherwise, it prints 'No'. After processing all test cases, the function concludes with no explicit return value, but the output consists of 'Yes' or 'No' for each test case.

