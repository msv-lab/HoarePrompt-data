#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a, b, and c are integers such that 0 <= a, b, c <= 9.
def func():
    q = int(input())
    mn = 100
    for i in range(q):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        
        if a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: t remains an integer such that 1 <= t <= 1000, a, b, and c are the last input integers such that 0 <= a, b, c <= 9, q is reduced by the number of iterations executed, mn remains 100.
#Overall this is what the function does:The function `func` reads an integer `q` from the input, where `1 <= q <= 1000`. It then processes `q` test cases, each consisting of three integers `a`, `b`, and `c` (where `0 <= a, b, c <= 9`). For each test case, it prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' in all other cases. After processing all test cases, the function does not return any value, and the variables `a`, `b`, and `c` are left with the values of the last test case. The variable `mn` remains unchanged at 100, and `q` is reduced by the number of test cases processed.

