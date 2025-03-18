#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. Each of the t test cases consists of three digits a, b, and c, where 0 ≤ a, b, c ≤ 9.
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
        
    #State: `t` is an integer input such that 1 ≤ `t` ≤ 1000; the loop has executed `t` times; for each of the `t` iterations, the program has read three integers `a`, `b`, and `c` from the input and printed either 'STAIR', 'PEAK', or 'NONE' based on the conditions `a < b < c` or `a < b > c`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` and prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise.

