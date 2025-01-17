from math import gcd
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().strip().split()))
    end=n-2
    for i in range(n-3,0,-1):
        if gcd(a[i],a[i+1])>gcd(a[i+1],a[i+2]):
            break
        end=i
    if end<2:
        print("Yes")
        continue
    falg=False
    for i in range(n):
        if not(i<3 or gcd(a[i-3],a[i-2])<=gcd(a[i-2],a[i-1])):
            break
        if i+1>=end and (i==1 or i==n-1 or gcd(a[i-2],a[i-1])<=gcd(a[i-1],a[i+1])) and (
        i>=n-2 or gcd(a[i - 1], a[i + 1])<=gcd(a[i+1],a[i+2])
        ):
            print("Yes")
            falg=True
            break
    if not falg:
        print("No")