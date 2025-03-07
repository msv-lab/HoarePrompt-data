#State of the program right berfore the function call: The function should be called with a list of test cases, where each test case is a tuple or list of three digits (a, b, c) such that 0 <= a, b, c <= 9, and the number of test cases t is an integer such that 1 <= t <= 1000.
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
        
    #State: `q` is greater than or equal to the number of iterations, `i` is `q - 1`, and for each iteration, `a`, `b`, and `c` are input integers. If `a < b < c`, then the condition `a < b < c` holds. If `a < b > c`, then the conditions `a < b` and `b > c` hold. Otherwise, none of the conditions `a < b < c` or `a < b > c` hold.
#Overall this is what the function does:The function `func` reads an integer `q` from the user input, which represents the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` from the user input. It then checks the relationship between these three integers and prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. After processing all test cases, the function does not return any value. The final state of the program is that `q` test cases have been processed, and the appropriate output has been printed for each case.

