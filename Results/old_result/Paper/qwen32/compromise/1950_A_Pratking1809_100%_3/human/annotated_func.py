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
        
    #State: t remains an integer such that 1 ≤ t ≤ 1000, and for each test case, the values of a, b, and c are not defined outside the loop as they are re-assigned in each iteration; q remains the same input integer. The output consists of 'STAIR', 'PEAK', or 'NONE' printed for each of the q iterations based on the conditions evaluated within the loop.
#Overall this is what the function does:The function reads an integer `q` representing the number of test cases, and for each test case, it reads three integers `a`, `b`, and `c` each ranging from 0 to 9. It then prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise.

