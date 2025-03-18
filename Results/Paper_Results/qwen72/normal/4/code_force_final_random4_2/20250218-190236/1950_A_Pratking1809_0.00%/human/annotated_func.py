#State of the program right berfore the function call: t is an integer where 1 <= t <= 1000, and for each test case, a, b, and c are digits where 0 <= a, b, c <= 9.
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
        
    #State: `t` is an integer where 1 <= t <= 1000, `a`, `b`, and `c` are digits where 0 <= a, b, c <= 9 and are assigned the values from the input, `q` is an input integer, `mn` is 100, `i` is `q - 1`. If `a < b > c`, the condition `a < b > c` is true. If `a < b < c`, the condition `a < b < c` is true. If neither `a < b < c` nor `a < b > c` is true, then both conditions are false.
#Overall this is what the function does:The function `func` reads an integer `q` from the input, representing the number of test cases. For each test case, it reads three digits `a`, `b`, and `c` from the input. It then checks the relationship between these digits and prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. The function does not return any value; it only prints the results to the console. After the function concludes, the input integer `q` and the digits `a`, `b`, and `c` for each test case are processed, and the final state of the program is that the results of the comparisons have been printed for all test cases.

