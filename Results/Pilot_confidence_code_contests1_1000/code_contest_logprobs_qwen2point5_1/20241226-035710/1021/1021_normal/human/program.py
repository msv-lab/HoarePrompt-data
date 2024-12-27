a = [None] * 1000
n=int(raw_input())
a=map(int, raw_input().split())
if n == 1:
    print(a[0])
    exit(0)
a.sort()
t = n-1
k = -1
while n:
    k += 1
    n -= 1
    if(n == 1):
        p = 1
        break
    n -= 1
    if(n == 1):
        p = 2
        break
    t -= 1
if p == 1:
    print(a[t-1])
else:
    print(a[k+1])
