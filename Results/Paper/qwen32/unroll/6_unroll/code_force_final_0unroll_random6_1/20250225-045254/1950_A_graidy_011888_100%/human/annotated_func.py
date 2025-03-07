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
        
    #State: The output state consists of `t` test cases, where for each test case, the program has printed either 'STAIR', 'PEAK', or 'NONE' based on the values of `a`, `b`, and `c` provided in the input. The values of `t`, `n`, and the initial values of `a`, `b`, and `c` remain unchanged.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` and prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. The values of `n`, `a`, `b`, and `c` remain unchanged after the function execution.

