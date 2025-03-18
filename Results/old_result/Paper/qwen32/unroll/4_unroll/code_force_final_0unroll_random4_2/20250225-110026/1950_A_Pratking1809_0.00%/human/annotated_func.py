#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each of the t test cases, a, b, and c are integers such that 0 <= a, b, c <= 9.
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
        
    #State: - The values of `t`, `mn`, and the state of any variables not involved in the loop remain unchanged.
    #   - The values of `a`, `b`, and `c` will be the values from the last iteration of the loop, as they are overwritten in each iteration.
    #   - The loop prints 'STAIR', 'PEAK', or 'NONE' for each iteration based on the input values, but these print statements do not affect the state of the variables.
    #
    #Given the above analysis, the output state will be:
    #
    #Output State:
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c`. It then prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. The function does not return any value; it only prints the result for each test case.

