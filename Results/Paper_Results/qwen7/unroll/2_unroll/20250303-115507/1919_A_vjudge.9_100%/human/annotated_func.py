#State of the program right berfore the function call: a and b are non-negative integers such that 1 <= a, b <= 10^9.
def func():
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: Output State: The output state consists of a series of lines, each containing either "Bob" or "Alice", depending on the input values for `a` and `b` in each iteration of the loop. Specifically, for each iteration `i` from `0` to `t-1`, if the absolute difference between `a` and `b` is even, the line will contain "Bob"; otherwise, it will contain "Alice". The values of `a` and `b` for each iteration are provided as input to the loop.
#Overall this is what the function does:The function reads a number `t` indicating the number of test cases. For each test case, it reads two non-negative integers `a` and `b` and prints "Bob" if the absolute difference between `a` and `b` is even, or "Alice" if the absolute difference is odd. The function does not return any value.

