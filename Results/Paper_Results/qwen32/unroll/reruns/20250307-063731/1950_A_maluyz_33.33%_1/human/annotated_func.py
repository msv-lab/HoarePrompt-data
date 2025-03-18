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
        
    #State: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, the output is either 'STAIR', 'PEAK', or 'NONE' based on the conditions provided.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` (where 0 ≤ a, b, c ≤ 9). It then prints 'STAIR' if `a < b < c`, 'PEAK' if `b` is the maximum of `a`, `b`, and `c`, and 'NONE' otherwise.

