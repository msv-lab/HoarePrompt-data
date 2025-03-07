#State of the program right berfore the function call: The function is expected to handle multiple test cases. Each test case consists of three digits a, b, and c, where 0 <= a, b, c <= 9. The number of test cases, t, is a positive integer such that 1 <= t <= 1000.
def func():
    q = int(input())
    for i in range(q):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: `q` is greater than 0, `i` is `q-1`, and `a`, `b`, and `c` are the input integers for the last iteration. If `a < b < c`, the current values of `a`, `b`, and `c` satisfy `a < b < c`. If `a < b > c`, the condition `a < b` and `b > c` holds. Otherwise, neither `a < b < c` nor `a < b > c` holds.
#Overall this is what the function does:The function `func` reads an integer `q` from the input, representing the number of test cases, where 1 <= q <= 1000. For each test case, it reads three integers `a`, `b`, and `c` (0 <= a, b, c <= 9). It then checks the relationship between these three integers and prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. After processing all test cases, the function concludes, and the final state is that `q` test cases have been processed, with the appropriate output printed for each case.

