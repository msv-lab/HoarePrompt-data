#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a, b, and c are integers such that 0 <= a, b, c <= 9.
def func():
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIRS')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: The values of `t`, `a`, `b`, and `c` remain unchanged, but the loop will have printed 'STAIRS', 'PEAK', or 'NONE' for each iteration based on the conditions provided.
#Overall this is what the function does:The function `func` reads an integer `t` from the user input, where `1 <= t <= 1000`, indicating the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` (where `0 <= a, b, c <= 9`). It then prints 'STAIRS' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. After processing all test cases, the function completes without modifying the values of `t`, `a`, `b`, or `c`.

