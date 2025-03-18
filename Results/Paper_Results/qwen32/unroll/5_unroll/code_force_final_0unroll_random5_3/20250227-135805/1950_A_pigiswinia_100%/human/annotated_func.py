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
        
    #State: t is the integer input provided, such that 1 ≤ t ≤ 1000
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, where 1 ≤ t ≤ 1000. For each test case, it reads three integers `a`, `b`, and `c` such that 0 ≤ a, b, c ≤ 9. It then prints "STAIR" if `a < b < c`, "PEAK" if `a < b > c`, and "NONE" for all other cases.

