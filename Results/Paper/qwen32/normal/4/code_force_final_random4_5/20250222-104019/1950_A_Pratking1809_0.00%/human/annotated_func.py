#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a, b, and c are integers such that 0 <= a, b, c <= 9.
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
        
    #State: `t` is an integer such that 1 <= t <= 1000, `a`, `b`, and `c` are the integers provided by the input from the last iteration, `q` is an integer representing the total number of iterations that have occurred, `i` is equal to `q - 1` (since `i` will be `q-1` after the loop has completed all `q` iterations), and `mn` is 100. No changes are made to `t`, `mn`, or any other variables outside of the loop body. The loop has finished executing all `q` iterations.
#Overall this is what the function does:The function reads an integer `q` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` and prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise.

