#State of the program right berfore the function call: The function should be called with a list of test cases, where each test case is a tuple of three digits (a, b, c) such that 0 <= a, b, c <= 9, and the number of test cases t is an integer such that 1 <= t <= 1000.
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
        
    #State: The loop will have executed `q` times, and for each iteration, it will have read three integers `a`, `b`, and `c` from the input. Depending on the values of `a`, `b`, and `c`, it will have printed either 'STAIR', 'PEAK', or 'NONE' to the console. The variables `a`, `b`, and `c` will be in their final state after the last iteration, but their specific values will depend on the last input provided. The variable `i` will have the value `q-1` after the loop finishes. The number of test cases `t` and the input integer `q` will remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `q` from the input, which represents the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` from the input. Depending on the values of `a`, `b`, and `c`, it prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. After executing `q` times, the function completes without returning any value. The variables `a`, `b`, and `c` will be in their final state after the last iteration, but their specific values will depend on the last input provided. The variable `i` will have the value `q-1` after the loop finishes. The input integer `q` remains unchanged.

