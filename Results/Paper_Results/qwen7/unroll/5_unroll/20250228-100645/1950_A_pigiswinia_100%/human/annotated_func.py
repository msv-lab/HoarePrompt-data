#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
def func():
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: Output State: The output state will consist of strings printed during each iteration of the loop based on the conditions provided. Specifically, for each line of input (a, b, c) where `i` ranges from 0 to `t-1`, the output will be either 'STAIR', 'PEAK', or 'NONE' depending on whether `a < b < c`, `a < b > c`, or neither condition is met, respectively.
#Overall this is what the function does:The function reads an integer `t` and then processes `t` sets of three integers `a`, `b`, and `c`. For each set, it prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. After processing all sets, the function concludes with no return value.

