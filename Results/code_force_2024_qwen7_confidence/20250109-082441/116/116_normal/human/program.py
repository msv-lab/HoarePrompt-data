t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    p= [0 for i in range(n)]
    p[0] = -1 
    for i in range(1,n):
        if a[i] != a[i -1]:
            p[i] = i - 1
        else:
            p[i] = p[i - 1]
    for i in range(q):
        l,r = map(int,input().split())
        l -= 1
        r -= 1
        if l <= p[r]:
            print(p[r] + 1,end=" ")
            print(r+1)
        else:
            print(-1,end=" ")
            print(-1)