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
        
    #State: The loop will execute t times, and for each iteration, it will read three integers a, b, and c from the input. Depending on the values of a, b, and c, it will print 'STAIR' if a < b < c, 'PEAK' if a < b > c, and 'NONE' otherwise. The values of a, b, and c will be updated for each iteration, but their final values after the loop will be the values read in the last iteration. The value of t will remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` (1 <= t <= 1000) from the input, which represents the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` (0 <= a, b, c <= 9) from the input. Depending on the values of `a`, `b`, and `c`, it prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. After executing `t` test cases, the function completes, and the final values of `a`, `b`, and `c` will be those read in the last test case, while the value of `t` remains unchanged.

