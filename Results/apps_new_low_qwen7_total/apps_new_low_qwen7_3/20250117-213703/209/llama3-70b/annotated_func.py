#State of the program right berfore the function call: The function receives no input parameters. However, the input data is expected to be read from standard input in the format specified in the problem description, and the output should be written to standard output in the format specified. The coordinates of the two known trees are distinct and lie within the range (-100, 100) for both x and y coordinates.
def func():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 == x2) :
        x3, x4 = x1 + abs(y1 - y2), x1 - abs(y1 - y2)

y3, y4 = y1, y2
    else :
        y3, y4 = y1 + abs(x1 - x2), y1 - abs(x1 - x2)

x3, x4 = x1, x2
    #State of the program after the if-else block has been executed: `x1`, `y1`, `x2`, `y2` are input integers. If `x1` equals `x2`, then `x3` is `2 * x1 - |y1 - y2|`, and `x4` is `-|y1 - y2|`. Otherwise, `x3` remains equal to `x1`, and `x4` remains equal to `x2`. `y3` is `y1 + |x1 - x2|`, and `y4` is `y1 - |x1 - x2|`.
    if (-1000 <= x3 <= 1000 and -1000 <= x4 <= 1000 and -1000 <= y3 <= 1000 and -
    1000 <= y4 <= 1000) :
        print(x3, y3, x4, y4)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: `x1`, `y1`, `x2`, `y2` are input integers. If `x1` equals `x2`, then `x3` is `2 * x1 - |y1 - y2|`, `x4` is `-|y1 - y2|`, `y3` is `y1 + |x1 - x2|`, and `y4` is `y1 - |x1 - x2|`, and the console prints `x3`, `y3`, `x4`, `y4`. Otherwise, `x3` remains equal to `x1`, `x4` remains equal to `x2`, `y3` is `y1 + |x1 - x2|`, and `y4` is `y1 - |x1 - x2|`, and the console prints `-1`.
#Overall this is what the function does:The function reads the coordinates of two trees from standard input, ensuring they are distinct and within the specified range (-100, 100). Based on whether the x-coordinates of the trees are equal, it calculates new coordinates (x3, x4, y3, y4) according to specific formulas. If the calculated coordinates are within the range [-1000, 1000], it prints these coordinates; otherwise, it prints -1. The function does not accept any parameters and returns nothing.

