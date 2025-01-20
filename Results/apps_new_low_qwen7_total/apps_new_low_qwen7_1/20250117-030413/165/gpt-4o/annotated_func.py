#State of the program right berfore the function call: y1, y2, yw, xb, yb, and r are integers, where y1, y2, yw > 0, y1 < y2 < yw, yb + r < yw, 2 * r < y2 - y1, and r > 0.
def func_1(y1, y2, yw, xb, yb, r):
    if (yb + r >= yw or y1 >= y2 or y1 + r >= y2 - r) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: y1, y2, yw, xb, yb, and r are integers, where y1, y2, yw > 0, y1 < y2 < yw, yb + r < yw, 2 * r < y2 - y1, and r > 0. Additionally, yb + r < yw, y1 < y2, and y1 + r < y2 - r.
    y_goal_mid = (y1 + y2) / 2
    if (y_goal_mid - r < y1 or y_goal_mid + r > y2) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: `y1` is an integer, `y2` is an integer, `yw` is an integer, `xb` is an integer, `yb` is an integer, `r` is an integer, `y_goal_mid` is an integer such that `y1 < y_goal_mid < y2` and `y_goal_mid - r >= y1 and y_goal_mid + r <= y2`
    x_w = xb - 2 * (yb - y_goal_mid) * (xb - 0) / (y_goal_mid - yb)
    if (x_w <= 0) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: `y1` is an integer, `y2` is an integer, `yw` is an integer, `xb` is an integer, `yb` is an integer, `r` is an integer, `y_goal_mid` is an integer such that `y1 < y_goal_mid < y2` and `y_goal_mid - r >= y1` and `y_goal_mid + r <= y2`, `x_w` is `xb - 2 * (yb - y_goal_mid) * (xb - 0) / (y_goal_mid - yb)`, and `x_w > 0`
    return x_w
    #`The program returns x_w which is calculated as xb - 2 * (yb - y_goal_mid) * (xb - 0) / (y_goal_mid - yb)` and is greater than 0
#Overall this is what the function does:The function `func_1` accepts six integers `y1`, `y2`, `yw`, `xb`, `yb`, and `r` with specific constraints and returns `-1` in three cases and a value `x_w` in the fourth case. Specifically, the function calculates `x_w` using the formula `xb - 2 * (yb - y_goal_mid) * (xb - 0) / (y_goal_mid - yb)` where `y_goal_mid` is the midpoint between `y1` and `y2`. The function returns `-1` if any of the following conditions are met:
1. `yb + r >= yw`
2. `y1 >= y2`
3. `y1 + r >= y2 - r`
4. `y_goal_mid - r < y1` or `y_goal_mid + r > y2`
5. `x_w <= 0`.

If none of these conditions are met, the function returns `x_w`, which is guaranteed to be greater than 0.

