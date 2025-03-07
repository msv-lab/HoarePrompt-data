#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b and b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 1000, `i` is 999 (since the loop runs from `range(n)` and `n` can be up to 1000), `a`, `b`, and `c` are integers obtained from the input split for the last iteration of the loop. The values of `t` and `a`, `b`, `c` remain unchanged throughout the loop executions as no assignment to these variables is done within the loop body.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \(a\), \(b\), and \(c\) where \(0 \leq a, b, c \leq 9\). For each test case, it determines whether the sequence \(a, b, c\) represents a 'STAIR' (if \(a < b < c\)), a 'PEAK' (if \(a < b\) and \(b > c\)), or 'NONE' otherwise. It prints the result for each test case. After processing all test cases, it outputs the final values of \(i\) (which will be 999 since the loop runs from `range(n)` and \(n\) can be up to 1000) and the values of \(a\), \(b\), and \(c\) from the last test case.

