#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, the program has printed either 'STAIR', 'PEAK', or 'NONE' based on the values of a, b, and c provided. The variables a, b, and c are no longer in a defined state as they are re-assigned in each iteration of the loop.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c`. It then prints 'STAIR' if `a < b < c`, 'PEAK' if `b` is the maximum of the three integers, and 'NONE' otherwise.

