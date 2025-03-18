for _ in range(int(input())):
    n = int(input())
    lit = list(map(int, input().split()))
    (a, b) = ([], [])
    cp = 0
    for i in range(0, n):
        if len(a) == 0:
            x = float('inf')
        else:
            x = a[-1]
        if len(b) == 0:
            y = float('inf')
        else:
            y = b[-1]
        if x > y:
            if y >= lit[i]:
                b.append(lit[i])
            elif lit[i] > x:
                b.append(lit[i])
            elif x >= lit[i] and lit[i] > y:
                a.append(lit[i])
        elif x == y:
            a.append(lit[i])
        elif x < y:
            if x >= lit[i]:
                a.append(lit[i])
            elif lit[i] > y:
                a.append(lit[i])
            elif y >= lit[i] and lit[i] > x:
                b.append(lit[i])
    s = 0
    for i in range(1, len(a)):
        if a[i] > a[i - 1]:
            s += 1
    for i in range(1, len(b)):
        if b[i] > b[i - 1]:
            s += 1
    print(s)