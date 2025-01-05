t = int(input())
r = []
for _ in range(t):
    n = int(input())

    cx = set()
    ax = int(1e9 + 7)
    bx = -1
    for _ in range(n):
        a, x = map(int, input().split())
        if a == 1:
            bx = max(x, bx)
        elif a == 2:
            ax = min(x, ax)
        else:
            cx.add(x)
    
    if bx >= ax:
        r.append(0)
    else:
        tmp = 0
        for i in cx:
            if i >= bx and i <= ax:
                tmp += 1
        r.append(ax - bx + 1 - tmp)

print(*r, sep="\n")