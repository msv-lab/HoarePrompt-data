#State of the program right berfore the function call: x_1, y_1, x_2, y_2 are integers within the range [-100, 100], and (x_1, y_1) ≠ (x_2, y_2).
def func():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 == x2) :
        x3, x4 = x1 + abs(y1 - y2), x1 - abs(y1 - y2)

y3, y4 = y1, y2
    else :
        y3, y4 = y1 + abs(x1 - x2), y1 - abs(x1 - x2)

x3, x4 = x1, x2
    #State of the program after the if-else block has been executed: *`x1`, `y1`, `x2`, `y2` are integers within the range [-100, 100], and (x1, y1) ≠ (x2, y2). If `x1 == x2`, `x3` is `x1 + abs(y1 - y2)`, `x4` is `x1 - abs(y1 - y2)`, `y3` is `y1`, and `y4` is `y2`. Otherwise, `x3` is `x1`, `y3` is `y1 + abs(x1 - x2)`, `x4` is `x2`, and `y4` is `y1 - abs(x1 - x2)`.
    if (-1000 <= x3 <= 1000 and -1000 <= x4 <= 1000 and -1000 <= y3 <= 1000 and -
    1000 <= y4 <= 1000) :
        print(x3, y3, x4, y4)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`x1`, `y1`, `x2`, `y2` are integers within the range [-100, 100], and (x1, y1) ≠ (x2, y2). If `x1 == x2`, `x3` is `x1 + abs(y1 - y2)`, `x4` is `x1 - abs(y1 - y2)`, `y3` is `y1`, and `y4` is `y2`. Otherwise, `x3` is `x1`, `y3` is `y1 + abs(x1 - x2)`, `x4` is `x2`, and `y4` is `y1 - abs(x1 - x2)`. If `x3`, `x4`, `y3`, and `y4` are all within the range [-1000, 1000], their values are printed. Otherwise, at least one of `x3`, `x4`, `y3`, or `y4` is outside the range [-1000, 1000].
#Overall this is what the function does:The function reads four integer values `x1`, `y1`, `x2`, `y2` from user input, where these integers are within the range [-100, 100] and `(x1, y1) ≠ (x2, y2)`. The function then calculates two new sets of coordinates, `(x3, y3)` and `(x4, y4)`, based on the following rules:
- If `x1 == x2`, then `x3 = x1 + abs(y1 - y2)`, `x4 = x1 - abs(y1 - y2)`, `y3 = y1`, and `y4 = y2`.
- If `x1 ≠ x2`, then `x3 = x1`, `x4 = x2`, `y3 = y1 + abs(x1 - x2)`, and `y4 = y1 - abs(x1 - x2)`.

After calculating these coordinates, the function checks if `x3`, `x4`, `y3`, and `y4` are all within the range [-1000, 1000]. If they are, the function prints `x3`, `y3`, `x4`, `y4`. If any of these values are outside the range, the function prints `-1`.

The function does not return any value; it only prints the results. The final state of the program is that the calculated coordinates are either printed or `-1` is printed, depending on whether the calculated coordinates fall within the specified range.

