from collections import Counter as C
for _ in range(int(input())):
    n,c,d = map(int,input().split())
    a = C(map(int,input().split()))
    mn = min(a)
    x = mn
    b = []
    for i in range(n):
        b.append(x)
        x+=c
    for i in range(n):
        x = b[i]
        for j in range(n):
            a[x]-=1
            x+=d
    for x in a.values():
        if x!=0:
            print("NO")
            break
    else:
        print("YES")
