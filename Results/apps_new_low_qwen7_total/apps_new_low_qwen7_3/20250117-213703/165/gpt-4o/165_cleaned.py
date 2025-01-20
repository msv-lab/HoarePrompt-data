def func_1(y1, y2, yw, xb, yb, r):
    if yb + r >= yw or y1 >= y2 or y1 + r >= y2 - r:
        return -1
    y_goal_mid = (y1 + y2) / 2
    if y_goal_mid - r < y1 or y_goal_mid + r > y2:
        return -1
    x_w = xb - 2 * (yb - y_goal_mid) * (xb - 0) / (y_goal_mid - yb)
    if x_w <= 0:
        return -1
    return x_w
input = sys.stdin.read
data = input().strip().split()
y1 = int(data[0])
y2 = int(data[1])
yw = int(data[2])
xb = int(data[3])
yb = int(data[4])
r = int(data[5])
result = func_1(y1, y2, yw, xb, yb, r)
if result == -1:
    print(result)
else:
    print(f'{result:.10f}')