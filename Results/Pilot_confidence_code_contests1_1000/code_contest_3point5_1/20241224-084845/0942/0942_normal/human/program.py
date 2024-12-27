while True:
    n, r = map(int, input().split())
    if n == 0 and r == 0:
        break

    l = []
    for i in range(1, n + 1):
        l.append(i)

    for i in range(0, r):
        p, c = map(int, input().split())
        tmp = l[len(l) - p + 1:len(l)]
        del l[len(l) - p + 1:len(l)]
        l[len(l) - c:len(l) - c] = tmp

    print(l[len(l) - 1])