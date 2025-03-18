#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
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
        
    #State: `i` is `t`, and `a`, `b`, `c` are the values from the last test case, with the final print statement being 'STAIRS', 'PEAK', or 'NONE' based on the last test case's values.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads three integers `a`, `b`, and `c`. It then prints 'STAIRS' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise.

