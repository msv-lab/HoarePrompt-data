#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a, b, c are integers such that 0 <= a, b, c <= 9.
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
        
    #State: `t` is an integer such that 1 <= t <= 1000, `q` is an integer such that 0 <= q <= 1000, `i` is `q-1`, `mn` is 100, and `a`, `b`, and `c` are integers provided by the user input. For each iteration, if `a < b < c`, the condition `a < b < c` holds true and 'STAIR' is printed. If `a < b > c`, the condition `a < b > c` holds true and 'PEAK' is printed. If neither `a < b < c` nor `a < b > c` holds true, 'NONE' is printed.
#Overall this is what the function does:The function `func` reads an integer `q` from user input, which represents the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` from user input. It then checks the relationship between these integers and prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. After processing all test cases, the function does not return any value, but the final state includes `q` as the number of test cases processed, `i` as `q-1` (the last index of the loop), and `mn` remains 100. The values of `a`, `b`, and `c` are not retained after each iteration.

