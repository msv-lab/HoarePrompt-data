n,x=map(int,raw_input().split())
a=(map(int,raw_input().split()))
b=[]
c=[]
d=[]
for i in range(n):
    if a[i] > x:
        b.append(a[i])
    elif a[i] == x:
        c.append(a[i])
    else:
        d.append(a[i])

if sum(a) == x:
    print(n)
elif len(b) == n:
    print(0)
elif len(c) == 1 and len(d) == 0:
    print(1)
else:
    print(len(d)-1)

