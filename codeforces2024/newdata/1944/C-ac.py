
from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    res = 0
    flag = 0
    for i in range(n):
        if c[i] == 0:
            res = i
            break
        elif c[i] == 1:
            if flag:
                break
            flag = 1
        res = i+1
    print(res)
