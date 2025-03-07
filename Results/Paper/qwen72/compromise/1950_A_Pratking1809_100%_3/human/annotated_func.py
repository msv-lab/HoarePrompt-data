#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a, b, and c are digits (integers) such that 0 <= a, b, c <= 9.
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
        
    #State: The values of t and q remain unchanged. For each iteration of the loop, the values of a, b, and c are updated based on user input, and the loop prints 'STAIR', 'PEAK', or 'NONE' depending on the conditions. After all iterations, the final values of a, b, and c are the last input values provided by the user.
#Overall this is what the function does:The function `func` processes a series of test cases, where the number of test cases is determined by user input. For each test case, it reads three digits `a`, `b`, and `c` from user input. It then prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. The function does not return any value; it only performs these print actions based on the conditions. After processing all test cases, the final values of `a`, `b`, and `c` are the last input values provided by the user.

