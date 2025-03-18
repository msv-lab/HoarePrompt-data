#State of the program right berfore the function call: The function is designed to handle multiple test cases. Each test case consists of three digits a, b, and c where 0 <= a, b, c <= 9. The number of test cases, t, is a positive integer such that 1 <= t <= 1000.
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
        
    #State: The values of `a`, `b`, and `c` are not retained after the loop finishes, and the variable `t` remains unchanged. The loop will have printed 'STAIR', 'PEAK', or 'NONE' for each test case based on the conditions provided.
#Overall this is what the function does:The function `func` accepts no parameters. It reads the number of test cases, `t`, from the user input, where `1 <= t <= 1000`. For each test case, it reads three digits `a`, `b`, and `c` from the user input, where `0 <= a, b, c <= 9`. After processing each test case, it prints 'STAIR' if `a < b < c`, 'PEAK' if `a <= b >= c` and `b` is the maximum, or 'NONE' otherwise. The function does not return any value, and the variables `a`, `b`, and `c` are not retained after each test case. The variable `t` remains unchanged after the function concludes.

