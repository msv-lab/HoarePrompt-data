t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    p=[l.count(j) for j in set(l)]
    if max(p)>=k:
        print(k-1)
    else:
        print(n)