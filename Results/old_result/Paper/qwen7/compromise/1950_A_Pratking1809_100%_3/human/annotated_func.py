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
        
    #State: Output State: The output state will consist of `q` lines, each containing either 'STAIR', 'PEAK', or 'NONE' based on the conditions evaluated for each set of inputs (a, b, c) provided in the loop. Each line corresponds to the output of one iteration of the loop, where `i` ranges from 0 to `q-1`. The initial values of `t` and `q` remain unchanged, but `t` is not used within the loop, so its value does not affect the output.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \(a\), \(b\), and \(c\) within the range 0 to 9. For each test case, it determines whether the sequence \(a, b, c\) represents a 'STAIR' (if \(a < b < c\)), a 'PEAK' (if \(a < b > c\)), or neither ('NONE'). It outputs one of these labels for each test case. The function does not return any value; instead, it prints the results directly to the console.

