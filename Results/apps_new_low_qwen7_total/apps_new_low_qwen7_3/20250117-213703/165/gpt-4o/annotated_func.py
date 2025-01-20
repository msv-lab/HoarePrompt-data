#State of the program right berfore the function call: y1, y2, yw, xb, yb, and r are integers such that 1 ≤ y1, y2, yw, xb, yb, r ≤ 10^6, y1 < y2 < yw, yb + r < yw, 2·r < y2 - y1, and the ball is positioned correctly in the field, doesn't cross any wall, and doesn't touch the wall that Robo-Wallace is aiming at.
def func_1(y1, y2, yw, xb, yb, r):
    if (yb + r >= yw or y1 >= y2 or y1 + r >= y2 - r) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: y1, y2, yw, xb, yb, and r are integers such that 1 ≤ y1, y2, yw, xb, yb, r ≤ 10^6, y1 < y2 < yw, yb + r < yw, 2·r < y2 - y1, and the ball is positioned correctly in the field, doesn't cross any wall, and doesn't touch the wall that Robo-Wallace is aiming at, yb + r < yw, y1 < y2, and y1 + r < y2 - r
    y_goal_mid = (y1 + y2) / 2
    if (y_goal_mid - r < y1 or y_goal_mid + r > y2) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: `y1` is an integer such that 1 ≤ `y1` < `y2` < `yw` ≤ 10^6, `y2` is an integer such that 1 ≤ `y1` < `y2` < `yw` ≤ 10^6, `yw` is an integer such that 1 ≤ `yw` ≤ 10^6, `xb` is an integer such that 1 ≤ `xb` ≤ 10^6, `yb` is an integer such that 1 ≤ `yb` ≤ 10^6, `r` is an integer such that 1 ≤ `r` ≤ 10^6, `y_goal_mid` = (`y1` + `y2`) / 2, and the ball is positioned correctly in the field, doesn't cross any wall, and doesn't touch the wall that Robo-Wallace is aiming at, `yb` + `r` < `yw`, `y1` < `y2`, and `y1` + `r` < `y2` - `r`, and (`y_goal_mid - r ≥ y1 and y_goal_mid + r ≤ y2`)
    x_w = xb - 2 * (yb - y_goal_mid) * (xb - 0) / (y_goal_mid - yb)
    if (x_w <= 0) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: `y1` is an integer such that 1 ≤ `y1` < `y2` < `yw` ≤ 10^6, `y2` is an integer such that 1 ≤ `y1` < `y2` < `yw` ≤ 10^6, `yw` is an integer such that 1 ≤ `yw` ≤ 10^6, `xb` is an integer such that 1 ≤ `xb` ≤ 10^6, `yb` is an integer such that 1 ≤ `yb` ≤ 10^6, `r` is an integer such that 1 ≤ `r` ≤ 10^6, `y_goal_mid` = (`y1` + `y2`) / 2, `x_w` is `xb - \frac{4 (yb - \frac{y1 + y2}{2}) \times xb}{y1 + y2 - 2yb}` and `x_w` > 0
    return x_w
    #`x_w` which is calculated as `xb - \frac{4 (yb - \frac{y1 + y2}{2}) \times xb}{y1 + y2 - 2yb}` and is greater than 0
#Overall this is what the function does:The function `func_1` accepts six parameters: `y1`, `y2`, `yw`, `xb`, `yb`, and `r`, all of which are integers constrained within the range \(1 \leq y1, y2, yw, xb, yb, r \leq 10^6\), with additional constraints \(y1 < y2 < yw\), \(yb + r < yw\), and \(2 \cdot r < y2 - y1\). The ball is also positioned correctly in the field, does not cross any wall, and does not touch the wall that Robo-Wallace is aiming at.

The function checks for several conditions:
1. If `yb + r >= yw`, `y1 >= y2`, or `y1 + r >= y2 - r`, the function returns -1.
2. If the midpoint between `y1` and `y2` (`y_goal_mid = (y1 + y2) / 2`) does not satisfy `y_goal_mid - r < y1` or `y_goal_mid + r > y2`, the function returns -1.
3. If the calculated value of `x_w` (where \(x_w = xb - \frac{4 (yb - \frac{y1 + y2}{2}) \times xb}{y1 + y2 - 2yb}\)) is less than or equal to 0, the function returns -1.

If none of the above conditions are met, the function calculates and returns `x_w`, ensuring it is greater than 0.

