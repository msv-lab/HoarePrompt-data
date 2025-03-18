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
        
    #State: The variables `a`, `b`, and `c` will hold the values from the last iteration of the loop, and `i` will be equal to `t`. The state of `t` remains unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads three integers `a`, `b`, and `c`. It then prints 'STAIR' if `a < b < c`, 'PEAK' if `b` is the maximum of the three integers, and 'NONE' otherwise. The function does not return any value; it only prints the results for each test case.

