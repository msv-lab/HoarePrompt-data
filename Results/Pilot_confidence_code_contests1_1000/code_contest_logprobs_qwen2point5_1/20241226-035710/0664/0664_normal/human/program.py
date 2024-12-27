l=[]
for i in range(int(raw_input())):
    x, y, n = map(int, raw_input().split())
    if n<x:
        l.append(0)
    else:
        a=(n//x)*x
        if a+y>n:
            l.append(a-(x-y))
        else:
            l.append(a+y)
for j in l:
    print(j)