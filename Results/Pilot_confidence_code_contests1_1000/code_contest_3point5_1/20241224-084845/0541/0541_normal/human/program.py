import sys

inp = [map(int, i.split(' ')) for i in sys.stdin.read().strip().splitlines()]

x, y, m = inp[0]

def check():
    global x, y, m
    return x >= m or y >= m

if x <= 0 and y <= 0:
    if check():
        res = 0
    else:
        res = -1
else:
    res = 0
    while not check():
        x, y = max(x, y), min(x, y)
        if x > 0 and y < 0 and abs(x) < abs(y):
            res += -y/x
            y += x*(-y/x)
        y += x
        res += 1

sys.stdout.write(str(res))
