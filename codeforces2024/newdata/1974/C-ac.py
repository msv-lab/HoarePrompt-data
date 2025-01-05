from collections import *
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    v1, v2, v3 = defaultdict(lambda: Counter()), defaultdict(lambda: Counter()), defaultdict(lambda: Counter())
    for i in range(1, n-1):
        v1[(a[i], a[i+1])][a[i-1]] += 1
        v2[(a[i-1], a[i+1])][a[i]] += 1
        v3[(a[i-1], a[i])][a[i+1]] += 1
    s = 0
    for i in v1:
        al = sum(v1[i].values())
        for j in v1[i]:
            s += v1[i][j]*(al-v1[i][j])
            al -= v1[i][j]
    for i in v2:
        al = sum(v2[i].values())
        for j in v2[i]:
            s += v2[i][j] * (al - v2[i][j])
            al -= v2[i][j]
    for i in v3:
        al = sum(v3[i].values())
        for j in v3[i]:
            s += v3[i][j]*(al-v3[i][j])
            al -= v3[i][j]
    print(s)