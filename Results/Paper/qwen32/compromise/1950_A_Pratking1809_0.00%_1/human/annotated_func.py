#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, `a`, `b`, and `c` are integers such that 0 ≤ a, b, c ≤ 9; `q` is an input integer; `mn` is 100. The loop has executed `q` times, and for each iteration, it has printed either 'STAIR', 'PEAK', or 'NONE' based on the comparison of `a`, `b`, and `c`.
#Overall this is what the function does:The function reads an integer `q` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` and prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise.

