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
        
    #State: Output State: The output state will consist of 'STAIRS', 'PEAK', or 'NONE' printed for each iteration of the loop based on the conditions provided. Specifically, for each input triplet (a, b, c), if \(a < b < c\), it prints 'STAIRS'; if \(a < b > c\), it prints 'PEAK'; otherwise, it prints 'NONE'. The exact sequence of these outputs depends on the user's input during each iteration.
#Overall this is what the function does:The function reads a number of test cases `t` and for each test case, it reads three integers `a`, `b`, and `c`. Based on the values of `a`, `b`, and `c`, it prints either 'STAIRS', 'PEAK', or 'NONE'. If `a < b < c`, it prints 'STAIRS'; if `a < b > c`, it prints 'PEAK'; otherwise, it prints 'NONE'. The function does not return any value.

