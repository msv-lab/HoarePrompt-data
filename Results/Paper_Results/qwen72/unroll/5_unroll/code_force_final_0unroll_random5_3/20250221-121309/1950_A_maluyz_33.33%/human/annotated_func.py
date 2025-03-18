#State of the program right berfore the function call: The function is expected to be called multiple times with different sets of three digits a, b, and c, where 0 <= a, b, c <= 9, and the total number of calls t is an integer such that 1 <= t <= 1000.
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
        
    #State: The values of `a`, `b`, and `c` will be the last set of three digits input by the user during the final iteration of the loop. The variable `t` will remain unchanged. The loop will have printed 'STAIR' for each set of inputs where `a < b < c`, 'PEAK' for each set where `b` is the maximum value, and 'NONE' for all other cases.
#Overall this is what the function does:The function `func` reads an integer `t` from user input, representing the number of test cases. For each of the `t` test cases, it reads three integers `a`, `b`, and `c` from user input. The function then prints 'STAIR' if `a < b < c`, 'PEAK' if `b` is the maximum value among `a`, `b`, and `c`, and 'NONE' for all other cases. After processing all test cases, the function completes without returning any value, and the values of `a`, `b`, and `c` will be the last set of inputs from the final iteration. The variable `t` remains unchanged.

