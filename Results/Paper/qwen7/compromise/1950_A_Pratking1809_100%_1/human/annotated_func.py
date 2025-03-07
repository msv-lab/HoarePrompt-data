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
        
    #State: Output State: The output state will consist of a series of lines, each containing either 'STAIR', 'PEAK', or 'NONE', based on the comparison of integers `a`, `b`, and `c` for each iteration of the loop. The number of lines will be equal to the value of `q`. Each line's content depends on the specific values of `a`, `b`, and `c` entered during each iteration.
#Overall this is what the function does:The function processes a series of test cases (determined by the integer `q`). For each test case, it reads three integers `a`, `b`, and `c` and prints one of three strings: 'STAIR', 'PEAK', or 'NONE', based on the relative values of `a`, `b`, and `c`. If `a < b < c`, it prints 'STAIR'. If `a < b > c`, it prints 'PEAK'. Otherwise, it prints 'NONE'. The function does not return any value.

