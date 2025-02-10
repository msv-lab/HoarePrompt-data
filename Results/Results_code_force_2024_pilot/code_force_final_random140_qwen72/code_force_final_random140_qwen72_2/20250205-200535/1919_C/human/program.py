for _ in range (int(input())):
    n = int(input());
    lit = list(map(int, input().split()));
    a, b = [lit[0]], [];
    cp = 0;
    for i in range (1, n):
        if a[-1] < lit[i]:
            b.append(lit[i]);
        else:
            a.append(lit[i]);
    s = 0;
    for i in range (1, len(a)):
        if a[i] > a[i-1]: s += 1;
    for i in range (1, len(b)):
        if b[i] > b[i-1]: s += 1;
    print (s);