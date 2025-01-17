t = int(input())
for _ in range(t):
    (a, b, c) = map(int, input().split())
    tents = a
    if b % 3 == 0:
        tents += b // 3
    elif b % 3 == 1:
        if c >= 2:
            tents += b // 3 + 1
            c -= 2
        else:
            print(-1)
            continue
    elif b % 3 == 2:
        if c >= 1:
            tents += b // 3 + 1
            c -= 1
        else:
            print(-1)
            continue
    if c >= 0:
        tents += c // 3 + (1 if c % 3 > 0 else 0)
        print(tents)
    else:
        print(-1)