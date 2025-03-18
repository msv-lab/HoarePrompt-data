#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
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
        
    #State: Output State: The output state will consist of strings ('STAIR', 'PEAK', or 'NONE') printed for each iteration of the loop based on the input values of `a`, `b`, and `c`. Each line's output depends on the comparison of these three integers.
#Overall this is what the function does:The function reads a number of test cases `t` and for each test case, it reads three integers `a`, `b`, and `c`. Based on the values of `a`, `b`, and `c`, it prints one of three strings: 'STAIR', 'PEAK', or 'NONE'. If `a < b < c`, it prints 'STAIR'. If `a == b == c`, it prints 'NONE'. If `b` is the maximum value among `a`, `b`, and `c`, it prints 'PEAK'. Otherwise, it prints 'NONE' for that test case.

