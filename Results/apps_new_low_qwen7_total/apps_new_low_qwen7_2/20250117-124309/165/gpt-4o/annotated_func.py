#State of the program right berfore the function call: y1, y2, yw, xb, yb, r are integers such that 1 ≤ y1, y2, yw, xb, yb ≤ 10^6, y1 < y2 < yw, yb + r < yw, 2·r < y2 - y1, and the ball is positioned correctly in the field, doesn't cross any wall, and doesn't touch the wall that Robo-Wallace is aiming at.
def func_1(y1, y2, yw, xb, yb, r):
    if (yb + r >= yw or y1 >= y2 or y1 + r >= y2 - r) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: y1, y2, yw, xb, yb, r are integers such that 1 ≤ y1, y2, yw, xb, yb ≤ 10^6, y1 < y2 < yw, yb + r < yw, 2·r < y2 - y1, and the ball is positioned correctly in the field, doesn't cross any wall, and doesn't touch the wall that Robo-Wallace is aiming at, and (yb + r < yw and y1 < y2 and y1 + r < y2 - r)
    y_goal_mid = (y1 + y2) / 2
    if (y_goal_mid - r < y1 or y_goal_mid + r > y2) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: `y1` is an integer such that 1 ≤ `y1` < `y2` ≤ 10^6, `y2` is an integer such that 1 < `y1` < `y2` ≤ 10^6, `yw`, `xb`, `yb`, `r` are integers, `y_goal_mid` is the arithmetic mean of `y1` and `y2`, `y1 < y2 < yw`, `yb + r < yw`, `2·r < y2 - y1`, and the ball is positioned correctly in the field, doesn't cross any wall, and doesn't touch the wall that Robo-Wallace is aiming at, and the condition `(y_goal_mid - r >= y1 and y_goal_mid + r <= y2)` holds.
    x_w = xb - 2 * (yb - y_goal_mid) * (xb - 0) / (y_goal_mid - yb)
    if (x_w <= 0) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: `y1` is an integer such that 1 ≤ `y1` < `y2` ≤ 10^6, `y2` is an integer such that 1 < `y1` < `y2` ≤ 10^6, `yw`, `xb`, `yb`, `r` are integers, `y_goal_mid` is the arithmetic mean of `y1` and `y2`, `y1 < y2 < yw`, `yb + r < yw`, `2·r < y2 - y1`, and the ball is positioned correctly in the field, doesn't cross any wall, and doesn't touch the wall that Robo-Wallace is aiming at, and the condition `(y_goal_mid - r >= y1 and y_goal_mid + r <= y2)` holds; `x_w` is `xb - (2 * yb - y1 - y2) * xb / (y1 + y2 - 2 * yb)`, and `x_w` is greater than 0
    return x_w
    #`The program returns x_w which is calculated as xb - (2 * yb - y1 - y2) * xb / (y1 + y2 - 2 * yb)`
#Overall this is what the function does:The function `func_1` accepts six parameters: `y1`, `y2`, `yw`, `xb`, `yb`, and `r`. It checks several conditions to ensure the ball is positioned correctly in the field, doesn't cross any wall, and doesn't touch the wall that Robo-Wallace is aiming at. If any of the conditions are violated, the function returns -1. Otherwise, it calculates and returns the value of `x_w` using the formula `xb - (2 * yb - y1 - y2) * xb / (y1 + y2 - 2 * yb)`.

