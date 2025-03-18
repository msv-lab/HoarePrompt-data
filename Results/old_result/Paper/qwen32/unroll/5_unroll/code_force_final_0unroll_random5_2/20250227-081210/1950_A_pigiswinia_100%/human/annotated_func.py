#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, a, b, and c are integers such that 0 <= a, b, c <= 9.
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
        
    #State: t is an integer provided by the input, where 1 <= `t` <= 1000; `a`, `b`, and `c` are not relevant as they are not retained after the loop.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads three integers `a`, `b`, and `c`. It then prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. The function does not return any value; it only prints the result for each test case.

