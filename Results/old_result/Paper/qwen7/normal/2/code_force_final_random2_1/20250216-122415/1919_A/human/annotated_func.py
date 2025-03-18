#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: Output State: `t` must be a positive integer less than or equal to 1000, `i` is equal to `t-1`, `a` and `b` are positive integers such that 1 ≤ `a`, `b` ≤ 10^9. The values of `a` and `b` are the last integers read from input during the loop's execution. For each iteration of the loop, if the absolute difference between `a` and `b` is even, the output was "Bob". If the absolute difference is odd, the output was "Alice". The variable `t` remains unchanged throughout the loop's execution, and `i` increments by 1 with each iteration until it reaches `t-1`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer `t` (1 ≤ t ≤ 1000) and two positive integers `a` and `b` (1 ≤ a, b ≤ 10^9). For each test case, it determines whether the absolute difference between `a` and `b` is even or odd and prints either "Bob" or "Alice" accordingly. After processing all test cases, the function does not return any value.

