#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each of the t test cases, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x < y:
            print(x, y)
        else:
            print(y, x)
        
    #State: t is an integer such that 1 ≤ t ≤ 100, x and y are the integers from the last iteration's input.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `x` and `y` and prints them in ascending order.

