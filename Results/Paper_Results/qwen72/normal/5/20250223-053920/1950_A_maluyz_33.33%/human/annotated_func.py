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
        
    #State: The loop has finished executing all iterations. The values of t, a, b, and c remain unchanged as they are input values. The output of the loop will be a series of 'STAIR', 'PEAK', or 'NONE' based on the conditions evaluated for each set of input values (a, b, c) provided during the iterations.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` from the user. Based on the values of `a`, `b`, and `c`, it prints 'STAIR' if `a < b < c`, 'PEAK' if `b` is the maximum of `a`, `b`, and `c`, and 'NONE' in all other cases. After processing all `t` test cases, the function completes, and the values of `t`, `a`, `b`, and `c` are not retained.

