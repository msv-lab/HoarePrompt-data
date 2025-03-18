#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a, b, and c are integers such that 0 <= a, b, c <= 9.
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
        
    #State: The loop will have executed t times, and for each iteration, it will have read three integers a, b, c from the input. Depending on the values of a, b, and c, it will have printed 'STAIR' if a < b < c, 'PEAK' if b is the maximum of a, b, and c, and 'NONE' in all other cases. The values of a, b, and c will be overwritten in each iteration, so their final values will be the ones from the last iteration.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of three integers `a`, `b`, and `c` (where 0 <= a, b, c <= 9). For each test case, it prints 'STAIR' if `a < b < c`, 'PEAK' if `b` is the maximum of `a`, `b`, and `c`, and 'NONE' in all other cases. After processing all test cases, the function does not return any value. The final state of the program is that `t` test cases have been processed, and the appropriate output has been printed for each test case.

