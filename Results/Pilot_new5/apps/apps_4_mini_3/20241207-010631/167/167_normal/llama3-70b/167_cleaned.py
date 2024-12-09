n = int(input())
a = list(map(int, input().split()))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def func_1(x, y):
    (px, py) = (0, 0)
    for v in a:
        (nx, ny) = ((v - 1) // y, (v - 1) % y)
        if abs(nx - px) + abs(ny - py) != 1:
            return False
        (px, py) = (nx, ny)
    return True
for x in range(1, 1000001):
    for y in range(1, 1000001):
        if x * y > max(a):
            break
        if all((1 <= v <= x * y for v in a)) and func_1(x, y):
            print('YES')
            print(x, y)
            exit()
print('NO')