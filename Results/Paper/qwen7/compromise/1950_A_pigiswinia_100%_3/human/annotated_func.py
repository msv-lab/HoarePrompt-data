#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
def func():
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: Output State: The output state will consist of `t` lines, each containing either 'STAIR', 'PEAK', or 'NONE', based on the comparison of integers `a`, `b`, and `c` provided by the user for each iteration of the loop. The value of `t` is determined by the initial integer input, and for each line, the output depends on the specific values of `a`, `b`, and `c` entered during that iteration.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, followed by `t` sets of three integers `a`, `b`, and `c`. For each set, it compares these integers and prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. After processing all test cases, it outputs `t` lines of results.

