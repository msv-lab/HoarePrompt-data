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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 1000, `i` is 999 (since the loop runs from `range(n)` and `n` can be up to 1000), `a`, `b`, and `c` are integers obtained from the input split for the last iteration of the loop. If `a < b < c` during any iteration, 'STAIR' is printed; if `a < b` and `b > c`, 'PEAK' is printed; otherwise, 'NONE' is printed. The values of `a`, `b`, and `c` do not change within the loop unless explicitly modified in the else block, but since no such modification is specified, they retain their input values from the last iteration.
    #
    #In simpler terms, after all iterations of the loop, `t` remains between 1 and 1000, `i` will be 999 (if `n` is set to its maximum value of 1000), and `a`, `b`, and `c` will be the values entered in the last input of the loop. The printed output will be 'STAIR', 'PEAK', or 'NONE' based on the conditions met during the iterations, with `a`, `b`, and `c` retaining their last input values.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers \(a\), \(b\), and \(c\) where \(0 \leq a, b, c \leq 9\). For each test case, it checks if \(a < b < c\) and prints 'STAIR', if \(a < b\) and \(b > c\) and prints 'PEAK', otherwise it prints 'NONE'. After processing all test cases, it outputs 'STAIR', 'PEAK', or 'NONE' based on the conditions met during the iterations. The function does not return any value but prints the result for each test case.

