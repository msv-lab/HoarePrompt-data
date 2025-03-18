#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
def func():
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a == b == c:
            print('NONE')
        elif max(a, b, c) == b:
            print('PEAK')
        else:
            print('NONE')
        
    #State: Output State: The output state will consist of strings printed during each iteration of the loop based on the comparison of three integers (`a`, `b`, and `c`) entered for each iteration. Specifically, for each line of input, if `a < b < c`, it prints 'STAIR'; if `a == b == c`, it prints 'NONE'; if `max(a, b, c) == b`, it prints 'PEAK'; otherwise, it prints 'NONE'. This process repeats `t` times, where `t` is the initial integer input.
#Overall this is what the function does:The function reads an integer `t` and then processes `t` test cases. For each test case, it reads three integers `a`, `b`, and `c`. Based on the values of these integers, it prints one of four possible outputs: 'STAIR', 'PEAK', 'NONE', or 'NONE' again depending on the specific conditions. After processing all `t` test cases, the function concludes without returning any value.

