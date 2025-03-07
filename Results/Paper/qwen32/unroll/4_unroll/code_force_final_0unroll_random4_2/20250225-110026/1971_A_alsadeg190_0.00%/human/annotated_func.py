#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each of the t test cases, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x > y:
            print(x, y)
        else:
            print(y, x)
        
    #State: t is an integer such that 1 ≤ t ≤ 100, x is the integer value of x from the last iteration of the loop, and y is the integer value of y from the last iteration of the loop.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases, where each test case consists of two integers `x` and `y`. For each test case, the function prints the two integers in non-decreasing order.

