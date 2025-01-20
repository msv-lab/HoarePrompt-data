#State of the program right berfore the function call: y1, y2, yw, xb, yb, r are integers such that 1 ≤ y1, y2, yw, xb, yb ≤ 10^6, y1 < y2 < yw, yb + r < yw, 2·r < y2 - y1.
def func_1(y1, y2, yw, xb, yb, r):
    if (yb + r >= yw or y1 >= y2 or y1 + r >= y2 - r) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: y1, y2, yw, xb, yb, r are integers such that 1 ≤ y1, y2, yw, xb, yb ≤ 10^6, y1 < y2 < yw, yb + r < yw, 2·r < y2 - y1, and (yb + r < yw and y1 < y2 and y1 + r < y2 - r)
    y_goal_mid = (y1 + y2) / 2
    if (y_goal_mid - r < y1 or y_goal_mid + r > y2) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: y1, y2, yw, xb, yb, r are integers such that 1 ≤ y1, y2, yw, xb, yb ≤ 10^6, y1 < y2 < yw, yb + r < yw, 2·r < y2 - y1, and (yb + r < yw and y1 < y2 and y1 + r < y2 - r), `y_goal_mid` is a float equal to `(y1 + y2) / 2`, and \( y_goal_mid - r \geq y1 \) and \( y_goal_mid + r \leq y2 \)
    x_w = xb - 2 * (yb - y_goal_mid) * (xb - 0) / (y_goal_mid - yb)
    if (x_w <= 0) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: *`y1, y2, yw, xb, yb, r` are integers such that 1 ≤ y1, y2, yw, xb, yb ≤ 10^6, y1 < y2 < yw, yb + r < yw, 2·r < y2 - y1, and (yb + r < yw and y1 < y2 and y1 + r < y2 - r); `y_goal_mid` is a float equal to `(y1 + y2) / 2`; \( y_goal_mid - r \geq y1 \) and \( y_goal_mid + r \leq y2 \); `x_w` is `3 * xb`, and `x_w` is greater than 0
    return x_w
    #The program returns `x_w` which is 3 times the value of `xb`, and `x_w` is greater than 0.
#Overall this is what the function does:The function `func_1` accepts six integer parameters `y1`, `2`, `yw`, `xb`, `yb`, and `r`. It checks several conditions and returns either `-1` or a calculated value `x_w`. Here's a summary of its behavior:

1.

