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
        
    #State: Output State: `t` must be exactly equal to the number of iterations the loop has executed, `i` is now `t-1`, `a`, `b`, and `c` are the last set of integers input by the user during the final iteration of the loop. The values of `a`, `b`, and `c` are integers obtained from the input split. Depending on the conditions met in the loop, the output printed during each iteration will be either 'STAIR', 'PEAK', or 'NONE'. After all iterations, the loop will have processed `t` sets of inputs, and the final values of `a`, `b`, and `c` will reflect the most recent input provided by the user.
#Overall this is what the function does:The function processes `t` sets of three integers (`a`, `b`, and `c`) and prints one of three possible outputs ('STAIR', 'PEAK', or 'NONE') for each set based on the values of `a`, `b`, and `c`. After processing all sets, the final values of `a`, `b`, and `c` represent the last set of integers input by the user. The function does not return any value.

