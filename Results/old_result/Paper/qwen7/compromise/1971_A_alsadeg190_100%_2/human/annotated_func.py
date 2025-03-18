#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x < y:
            print(x, y)
        else:
            print(y, x)
        
    #State: Output State: The values of `t` and `x` remain unchanged, and the output consists of pairs of integers printed based on the condition in the loop. For each iteration `i` from `0` to `x-1`, the program reads two integers `x` and `y` from input. If `x` is less than `y`, it prints `x` and `y`; otherwise, it prints `y` and `x`.
#Overall this is what the function does:The function processes a series of test cases defined by an integer `t`. For each test case, it reads two integers `x` and `y` from input. It then prints either `(x, y)` if `x` is less than `y`, or `(y, x)` otherwise. After processing all test cases, the function does not return any value but prints the results of each comparison.

