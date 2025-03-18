#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x > y:
            print(x, y)
        else:
            print(y, x)
        
    #State: Output State: The output state will consist of a series of pairs of integers printed based on the comparison within the loop. For each iteration `i` in the range of `x`, the program reads two integers from input, compares them, and prints them in descending order if `x > y`, or in ascending order otherwise. The final output state will be these printed pairs.
#Overall this is what the function does:The function processes an integer `t` (1 ≤ t ≤ 100) representing the number of test cases. For each test case, it reads two integers `x` and `y` (0 ≤ x, y ≤ 9), compares them, and prints either `(x, y)` in descending order if `x > y`, or `(y, x)` in ascending order if `x ≤ y`. After processing all test cases, it concludes with no return value.

