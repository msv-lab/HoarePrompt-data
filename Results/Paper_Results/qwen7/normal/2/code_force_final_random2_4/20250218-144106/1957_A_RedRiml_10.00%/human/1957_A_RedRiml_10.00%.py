w = int(input())
for _ in range(w):
    ln = int(input())
    palka = list(map(int, input().split()))
    pl = []
    d = {}
    for i in palka:
        if d.get(i) == None:
            d[i] = 1
        else:
            d[i] += 1
        if i not in pl:
            pl.append(i)
    shapes = 0
    for j in pl:
        if d[j] >= 3:
            shapes += 1
    print(shapes)