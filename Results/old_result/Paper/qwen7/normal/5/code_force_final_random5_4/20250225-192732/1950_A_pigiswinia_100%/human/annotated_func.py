#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
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
        
    #State: Output State: `t` is a value between 1 and 1000, `i` is 999 (since the loop runs from `i` in range(t) and `i` will reach `t-1`), `a`, `b`, and `c` are integers entered by the user for each iteration of the loop. After all iterations, regardless of the conditions `a < b < c` or `a < b > c` being met or not, the values of `t` and `i` will be as described, and `a`, `b`, and `c` will hold the last set of values entered by the user before the loop terminates.
#Overall this is what the function does:The function processes `t` test cases, where for each test case, it reads three integers `a`, `b`, and `c`. Based on the values of `a`, `b`, and `c`, it prints either 'STAIR', 'PEAK', or 'NONE'. After processing all test cases, it outputs the results for each case.

