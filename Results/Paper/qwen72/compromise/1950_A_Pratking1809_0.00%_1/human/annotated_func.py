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
        
    #State: t is an integer where 1 <= t <= 1000, a, b, and c are digits where 0 <= a, b, c <= 9, q is an input integer, mn is 100.
#Overall this is what the function does:The function `func` reads an integer `q` from the user, which represents the number of test cases. For each test case, it reads three digits `a`, `b`, and `c` from the user. It then checks the relationship between these digits and prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. The function does not return any value. After the function concludes, the integer `q` and the digits `a`, `b`, and `c` are no longer relevant, and the program state is unchanged except for the output printed to the console.

