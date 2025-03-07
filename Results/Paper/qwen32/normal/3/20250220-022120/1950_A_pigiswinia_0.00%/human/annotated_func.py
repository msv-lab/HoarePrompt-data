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
        
    #State: t is the integer input provided by the user such that \(1 \leq t \leq 1000\); a, b, and c are the integers input by the user such that \(0 \leq a, b, c \leq 9\); i is t-1. For each of the t iterations, the program has printed either 'STAIRS', 'PEAK', or 'NONE' based on the conditions a < b < c, a < b > c, or neither, respectively.
#Overall this is what the function does:The function accepts an integer `t` (1 ≤ t ≤ 1000) representing the number of test cases. For each test case, it accepts three integers `a`, `b`, and `c` (0 ≤ a, b, c ≤ 9). It prints 'STAIRS' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' if neither condition is met.

