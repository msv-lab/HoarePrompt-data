#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
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
        
    #State: - After all iterations, the only variable that changes is the output to the console (standard output). The variable `t` remains unchanged as it only determines the number of iterations.
    #   - The variables `a`, `b`, and `c` are re-assigned in each iteration and do not retain their values after the loop completes.
    #
    #Thus, the output state is solely defined by the series of printed strings ('STAIR', 'PEAK', or 'NONE') that occur during each iteration of the loop. Since the exact values of `a`, `b`, and `c` are not specified, we cannot determine the exact sequence of printed strings, but we know that `t` remains unchanged.
    #
    #Output State:
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c`. It then prints 'STAIR' if `a < b < c`, 'PEAK' if `b` is the maximum of the three integers, and 'NONE' otherwise. The function does not return any value; it only prints to the console.

