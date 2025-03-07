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
        
    #State: The values of `a`, `b`, and `c` will be the last set of integers input during the loop's final iteration. The value of `t` and `q` will remain unchanged. The loop will have printed 'STAIR', 'PEAK', or 'NONE' for each set of inputs based on the conditions provided.
#Overall this is what the function does:The function reads an integer `q` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` and prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise.

