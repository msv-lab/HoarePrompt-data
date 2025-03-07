#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    t = input()
    x = []
    y = []
    for i in range(10):
        xylist = input().split(' ')
        
        x.append(int(xylist[0]))
        
        y.append(int(xylist[1]))
        
    #State: Output State: `t` is an integer between 1 and 100 inclusive, `x` is a list containing 10 elements `[xylist[0], int(xylist[1]), int(xylist[0]), int(xylist[0]), int(xylist[1]), int(xylist[1]), int(xylist[0]), int(xylist[0]), int(xylist[1]), int(xylist[1])]`, `y` is a list containing 9 elements `int(xylist[1]), int(xylist[1]), int(xylist[1]), int(xylist[1]), int(xylist[1]), int(xylist[1]), int(xylist[1]), int(xylist[1]), int(xylist[1])`, `i` is 9, `xylist` is a list containing the split input values from the last iteration of the loop.
    #
    #This means that after the loop has executed all 10 iterations, the list `x` will contain 10 elements where the first element is the first value of `xylist`, the second element is the second value of `xylist` converted to an integer, the third element is the first value of `xylist` again, and so on, alternating between the first and second values of `xylist`. The list `y` will contain 9 elements, each being the second value of `xylist` from the respective iteration.
    for i in range(10):
        if x[i] < y[i]:
            print(x[i], ' ', y[i])
        else:
            print(y[i], ' ', x[i])
        
    #State: `t` is an integer between 1 and 100 inclusive, `x` is a list containing 10 elements `[xylist[0], int(xylist[1]), int(xylist[0]), int(xylist[0]), int(xylist[1]), int(xylist[1]), int(xylist[0]), int(xylist[0]), int(xylist[1]), int(xylist[1])]`, `y` is a list containing 9 elements `int(xylist[1]), int(xylist[1]), int(xylist[1]), int(xylist[1]), int(xylist[1]), int(xylist[1]), int(xylist[1]), int(xylist[1]), int(xylist[1])`, `i` is 9, and the loop has completed all 10 iterations without changing any elements in lists `x` or `y` based on the comparison conditions.
#Overall this is what the function does:The function reads an integer `t` and 10 pairs of integers `(x, y)` from the standard input. It then prints 10 lines, each containing two integers. For each pair, if the first integer (`x`) is less than the second integer (`y`), it prints `x` followed by `y`; otherwise, it prints `y` followed by `x`. After processing all pairs, the function does not return anything but modifies the lists `x` and `y` in place.

