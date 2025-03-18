for i in range(int(input())):
    n,m,k=map(int,input().split())
    M=10**9+7
    c=pow(n*(n-1)//1,-1,M)
    s=0
    a=0
    for i in range(m):
        u,v,f=map(int,input().split())
        a+=f
    for i in range(k):
        s=s+c*i*c*m+c*a
    print(s%M)