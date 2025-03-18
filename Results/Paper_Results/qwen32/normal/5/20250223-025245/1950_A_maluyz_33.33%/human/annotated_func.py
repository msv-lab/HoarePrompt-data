#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. Each of the t test cases consists of three digits a, b, and c, where 0 ≤ a, b, c ≤ 9.
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
        
    #State: The loop has executed `t` times, where `t` is the integer input by the user, and for each iteration, the program prints 'STAIR' if `a < b < c`, 'NONE' if `a == b == c`, 'PEAK' if `b` is the maximum among `a`, `b`, and `c`, and 'NONE' otherwise. The values of `t`, `a`, `b`, and `c` are not retained after the loop ends; only the printed outputs remain.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases. For each test case, it reads three digits `a`, `b`, and `c` (each between 0 and 9 inclusive) and prints 'STAIR' if `a < b < c`, 'NONE' if `a == b == c`, 'PEAK' if `b` is the maximum among `a`, `b`, and `c`, and 'NONE' otherwise.

