#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x > y:
            print(x, y)
        else:
            print(y, x)
        
    #State: Output State: The output state will consist of pairs of integers printed based on the condition in the loop. For each iteration `i` in the range of `x`, the program reads two integers from input, `x` and `y`. If `x` is greater than `y`, it prints `x` followed by `y`; otherwise, it prints `y` followed by `x`. The exact pairs printed depend on the inputs provided during each iteration.
#Overall this is what the function does:The function processes an integer `t` (1 ≤ t ≤ 100) representing the number of test cases. For each test case, it reads two integers `x` and `y` (0 ≤ x, y ≤ 9). Based on the comparison between `x` and `y`, it prints either `x, y` or `y, x`. After processing all test cases, the function does not return any value but outputs pairs of integers as specified.

