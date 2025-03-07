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
        
    #State: Output State: The output state will consist of a series of lines, each containing either 'STAIR', 'PEAK', or 'NONE', depending on the input values for each iteration of the loop. Specifically, for each line `i` (where `0 ≤ i < n`), the output will contain the result of the condition check based on the integers `a`, `b`, and `c` provided as input for that iteration. The initial values of `t` and `n` remain unchanged, and the output will reflect the results of the loop's execution based on the inputs given during each iteration.
#Overall this is what the function does:The function reads a series of test cases from the standard input, where each test case consists of three integers \(a\), \(b\), and \(c\). For each test case, it determines whether the sequence \(a\), \(b\), \(c\) represents a 'STAIR' (if \(a < b < c\)), a 'PEAK' (if \(a < b\) and \(b > c\)), or neither ('NONE'). It then prints the corresponding label for each test case. The function does not return any value and leaves the input variables unchanged after its execution.

