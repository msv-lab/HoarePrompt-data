t = int(input())
for j in range(t):
    b = input().split()
    n = int(b[0])
    k = int(b[1])
    l = list(map(int, input().split()))
    suf = []
    suf.append(0)
    for i in range(n):
        suf.append(suf[i] + l[i])
    smin = [0]
    for i in range(n):
        if suf[i + 1] < smin[i]:
            smin.append(suf[i + 1])
        else:
            smin.append(smin[i])
    sm = -111
    for i in range(n + 1):
        if suf[i] - smin[i] > sm or sm == -111:
            sm = suf[i] - smin[i]
    sm = 2 ** k * sm - sm
    sm += suf[n]
    if sm < 0:
        a = abs(sm) // (10 ** 9 + 7)
        sm += (a + 1) * (10 ** 9 + 7)
    else:
        sm = sm % (10 ** 9 + 7)
    print(sm)