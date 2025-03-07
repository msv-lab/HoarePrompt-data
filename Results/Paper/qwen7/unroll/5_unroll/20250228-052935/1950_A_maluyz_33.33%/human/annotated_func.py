#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
def func():
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a == b == c:
            print('NONE')
        elif max(a, b, c) == b:
            print('PEAK')
        else:
            print('NONE')
        
    #State: Output State: The output state will consist of strings printed during each iteration of the loop based on the conditions provided. For each iteration, if `a < b < c`, it prints 'STAIR'; if `a == b == c`, it prints 'NONE'; if `max(a, b, c) == b`, it prints 'PEAK'; otherwise, it prints 'NONE'. The exact sequence of these strings depends on the input values provided for each iteration.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \(a\), \(b\), and \(c\) (where \(0 \leq a, b, c \leq 9\)), and prints one of four possible outcomes: 'STAIR', 'PEAK', 'NONE', or 'NONE' again depending on the relationship between \(a\), \(b\), and \(c\). It accepts no parameters and does not return any value; instead, it outputs strings based on the conditions met by the input values.

