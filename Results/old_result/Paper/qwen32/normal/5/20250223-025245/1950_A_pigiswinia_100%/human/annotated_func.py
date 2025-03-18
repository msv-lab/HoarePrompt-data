#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
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
        
    #State: After all iterations, `t` remains the same, `i` is equal to `t - 1`, and for each of the `t` test cases, the appropriate output ('STAIR', 'PEAK', or 'NONE') has been printed based on the conditions involving `a`, `b`, and `c`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each of the `t` test cases, it reads three integers `a`, `b`, and `c` (each between 0 and 9 inclusive). It then prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' for all other cases.

