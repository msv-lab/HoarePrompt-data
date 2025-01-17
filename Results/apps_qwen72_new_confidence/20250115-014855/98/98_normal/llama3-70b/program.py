n, m, x, y, vx, vy = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if vx == 0:
    if vy == 0:
        print(-1)
    elif vy > 0:
        print(m, y + (m - y) // abs(vy) * vy)
    else:
        print(0, y - y // abs(vy) * vy)
elif vy == 0:
    if vx > 0:
        print(x + (n - x) // abs(vx) * vx, 0)
    else:
        print(0, x - x // abs(vx) * vx)
else:
    g = gcd(abs(vx), abs(vy))
    vx //= g
    vy //= g
    if vx > 0:
        dx = (n - x) // vx
    else:
        dx = -x // -vx
    if vy > 0:
        dy = (m - y) // vy
    else:
        dy = -y // -vy
    if dx == dy:
        print(n, m)
    elif dx < dy:
        print(n, y + dx * vy)
    else:
        print(x + dy * vx, m)
