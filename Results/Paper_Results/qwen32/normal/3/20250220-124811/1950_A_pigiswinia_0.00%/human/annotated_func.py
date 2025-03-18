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
        
    #State: `t` is an integer input by the user such that 1 ≤ `t` ≤ 1000, `i` is `t-1`, and for each of the `t` test cases, the program has read integers `a`, `b`, and `c` from the input. For each test case, the program has printed 'STAIRS' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c`. It then prints 'STAIRS' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise.

