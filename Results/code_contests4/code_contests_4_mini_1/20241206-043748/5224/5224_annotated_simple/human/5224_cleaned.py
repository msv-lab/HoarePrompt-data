n = input()
for i in xrange(n):
    (xa, ya, ra, xb, yb, rb) = map(int, raw_input().split())
    d = (xa - xb) ** 2 + (ya - yb) ** 2
    if d > (ra + rb) ** 2:
        print(0)
    elif ra > rb:
        if (ra - rb) ** 2 > d:
            print(2)
        else:
            print(1)
    elif (rb - ra) ** 2 > d:
        print(-2)
    else:
        print(1)