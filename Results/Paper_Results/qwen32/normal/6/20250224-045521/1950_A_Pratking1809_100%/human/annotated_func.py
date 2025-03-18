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
        
    #State: The loop has executed `q` times, and `t` remains unchanged as an integer such that 1 <= t <= 1000. For each of the `q` iterations, the user has input integers `a`, `b`, and `c` such that 0 <= a, b, c <= 9. The loop has printed 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. The variables `a`, `b`, and `c` are updated with the values from the last iteration, but their values after the loop ends are not relevant to the output state.
#Overall this is what the function does:The function reads an integer `q` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` each ranging from 0 to 9. It then prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise.

