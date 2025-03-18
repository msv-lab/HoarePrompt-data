#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a, b, and c are integers such that 0 <= a, b, c <= 9.
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
        
    #State: `t` is an integer such that 1 <= t <= 1000, `a`, `b`, and `c` are integers provided by the user input, `q` must be greater than or equal to the number of iterations, and `i` is `q - 1`. For each iteration, if `a < b < c`, then `a` is less than `b` which is less than `c`. If `a < b < c` is not true, then the relationship between `a`, `b`, and `c` does not satisfy `a < b < c`. If `a < b > c` is true, then `b` is greater than both `a` and `c`. If `a < b > c` is false, then the relationship between `a`, `b`, and `c` does not satisfy `a < b > c`.
#Overall this is what the function does:The function `func` reads an integer `q` from user input, representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` from user input. It then checks the relationship between these integers and prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. After processing all test cases, the function does not return any value. The final state of the program is that `q` test cases have been processed, and the appropriate output has been printed for each case.

