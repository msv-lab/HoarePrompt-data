for i in range(int(input())):
    n,m,k = map(int,input().split())
    l = list(map(int,input().split()))
    l.sort()
    
    s = 0
    c = (k*k)/2
 
    for i in range(n):
        s = min(m,k)
        k -= s
        c += l[i] * s - (s*s)/2
    print(int(c))