#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a, b, and c are integers such that 0 <= a, b, c <= 9.
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
        
    #State: The values of `t`, `a`, `b`, and `c` remain unchanged, but the loop will have printed 'STAIR', 'PEAK', or 'NONE' for each test case based on the conditions `a < b < c`, `a < b > c`, or neither, respectively.
#Overall this is what the function does:The function `func` takes no parameters and reads an integer `t` from the input, where `1 <= t <= 1000`. For each of the `t` test cases, it reads three integers `a`, `b`, and `c` (each between 0 and 9) from the input. It then prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. The function does not return any value. After the function concludes, the values of `t`, `a`, `b`, and `c` are not retained, and the only effect is the output of 'STAIR', 'PEAK', or 'NONE' for each test case.

