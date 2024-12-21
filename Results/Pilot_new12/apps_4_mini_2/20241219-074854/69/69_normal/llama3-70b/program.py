n = int(input())
ops = input()
x, y = map(int, input().split())

ux, uy, lx, ly = 0, 0, 0, 0
for op in ops:
    if op == 'U':
        uy += 1
    elif op == 'D':
        uy -= 1
    elif op == 'R':
        ux += 1
    elif op == 'L':
        ux -= 1

dx, dy = x - ux, y - uy
if dx < 0 or dy < 0:
    print(-1)
else:
    res = 0
    for op in ops:
        if op == 'U' and dy > 0:
            dy -= 1
        elif op == 'D' and dy < 0:
            dy += 1
        elif op == 'R' and dx > 0:
            dx -= 1
        elif op == 'L' and dx < 0:
            dx += 1
        else:
            res += 1
    print(res)
