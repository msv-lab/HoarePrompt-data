#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each of the t test cases, x and y are integers such that 0 <= x, y <= 9.
def func():
    t = input()
    x = []
    y = []
    for i in range(10):
        xylist = input().split(' ')
        
        x.append(int(xylist[0]))
        
        y.append(int(xylist[1]))
        
    #State: t is a string representation of an integer such that 1 <= int(t) <= 100, and x is a list of 10 integers, and y is a list of 10 integers.
    for i in range(10):
        if x[i] < y[i]:
            print(x[i], ' ', y[i])
        else:
            print(y[i], ' ', x[i])
        
    #State: t is a string representation of an integer such that 1 <= int(t) <= 100, and x is a list of 10 integers, and y is a list of 10 integers.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, then for each of 10 test cases, it reads two integers `x` and `y`. It prints the smaller of the two integers followed by the larger one.

