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
        
    #State: Output State: The output state will consist of a series of lines, each containing either 'STAIR', 'PEAK', or 'NONE', depending on the input values for each iteration of the loop. Specifically, for each line `i` (where `0 ≤ i < n`), the output will contain the result of the condition checks based on the integers `a`, `b`, and `c` entered for that iteration. The initial values of `t` and `n` remain unchanged, and the output will reflect the results of the specified conditions for each set of inputs provided within the loop.
#Overall this is what the function does:The function processes `n` sets of three integers `a`, `b`, and `c` (each between 0 and 9) and outputs one of three strings ('STAIR', 'PEAK', or 'NONE') for each set based on the given conditions. The function does not return any value. The initial values of `t` and `n` remain unchanged after the function executes.

