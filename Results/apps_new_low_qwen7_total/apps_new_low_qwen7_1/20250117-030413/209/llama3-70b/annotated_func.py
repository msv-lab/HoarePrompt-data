#State of the program right berfore the function call: The input consists of four space-separated integers x_1, y_1, x_2, y_2, where -100 ≤ x_1, y_1, x_2, y_2 ≤ 100 and x_1, y_1, x_2, y_2 are distinct. The coordinates represent the positions of two out of the four vertices of a square.
def func():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 == x2) :
        x3, x4 = x1 + abs(y1 - y2), x1 - abs(y1 - y2)

y3, y4 = y1, y2
    else :
        y3, y4 = y1 + abs(x1 - x2), y1 - abs(x1 - x2)

x3, x4 = x1, x2
    #State of the program after the if-else block has been executed: *`x1`, `y1`, `x2`, `y2`, `x3`, `y3`, `x4`, `y4` are integers. If `x1` is equal to `x2`, then `x3` is set to `x1 + |y1 - y2|`, `x4` is set to `x1 - |y1 - y2|`, and `y3` and `y4` remain unchanged as `y1` and `y2`. Otherwise, `x3` remains unchanged as `x1`, `x4` remains unchanged as `x2`, and `y3` is set to `y1 + |x1 - x2|`, `y4` is set to `y1 - |x1 - x2|`.
    if (-1000 <= x3 <= 1000 and -1000 <= x4 <= 1000 and -1000 <= y3 <= 1000 and -
    1000 <= y4 <= 1000) :
        print(x3, y3, x4, y4)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`x3`, `x4`, `y3`, `y4` are integers. If `x1 == x2`, then `x3` is `x1 + |y1 - y2|`, `x4` is `x1 - |y1 - y2|`, `y3` is `y1`, and `y4` is `y2`. Otherwise, `x3` is `x1`, `x4` is `x2`, `y3` is `y1 + |x1 - x2|`, and `y4` is `y1 - |x1 - x2|`. Additionally, `x3`, `x4`, `y3`, and `y4` are all within the range [-1000, 1000].
#Overall this is what the function does:The function `func` accepts no parameters directly but instead takes four space-separated integers `x_1`, `y_1`, `x_2`, `y_2` as input, where -100 ≤ `x_1`, `y_1`, `x_2`, `y_2` ≤ 100 and `x_1`, `y_1`, `x_2`, `y_2` are distinct. The coordinates represent the positions of two out of the four vertices of a square. After processing, the function determines whether these coordinates form a valid square by calculating the other two vertices based on the given coordinates. If the calculated coordinates (`x3`, `y3`, `x4`, `y4`) are within the range [-1000, 1000], it prints these coordinates; otherwise, it prints `-1`. The function does not return any value explicitly but provides output based on the validity of the input coordinates.

