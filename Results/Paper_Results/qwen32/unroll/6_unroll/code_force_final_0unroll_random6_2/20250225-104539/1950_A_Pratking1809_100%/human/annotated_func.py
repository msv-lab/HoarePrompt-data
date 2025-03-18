#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9; q is an input integer. After executing the loop, no changes are made to t, q, or the input values of a, b, and c, but the program will have printed 'STAIR', 'PEAK', or 'NONE' for each of the q iterations based on the conditions provided.
#Overall this is what the function does:The function reads an integer `q` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` (each between 0 and 9). It then prints 'STAIR' if `a` is less than `b` and `b` is less than `c`, prints 'PEAK' if `a` is less than `b` and `b` is greater than `c`, and prints 'NONE' otherwise. The function does not return any value; it only prints the result for each test case.

