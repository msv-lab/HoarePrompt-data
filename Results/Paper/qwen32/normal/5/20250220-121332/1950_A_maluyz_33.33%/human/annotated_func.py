#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each of the t test cases, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
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
        
    #State: The loop has executed `t` times, and for each iteration, it has read three integers `a`, `b`, and `c` from the input. Depending on the values of `a`, `b`, and `c`, it prints either 'STAIR', 'PEAK', or 'NONE'. The variable `i` has been incremented from 0 to `t-1`. The values of `a`, `b`, and `c` are the last set of integers read in the final iteration.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` and prints 'STAIR' if `a < b < c`, 'PEAK' if `b` is the maximum of the three integers, and 'NONE' otherwise.

