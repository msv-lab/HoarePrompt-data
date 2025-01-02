from bisect import bisect_left as p
z=lambda: map(int, raw_input().split())
n=input()
a=[z()+[i] for i in range(n)]
b=[-1]*n
w=0
a.sort()
for i in range(input()):
    x,y=z()
    h=p(a,[x])
    for u in (h-1,h):
        if 0<=u<n and (x-a[u][0])**2+y**2<=a[u][1]**2:
            d=a[u][2]
            if b[d]==-1:
                b[d]=i+1
                w+=1
print(w)
print(' '.join(map(str,b)))
