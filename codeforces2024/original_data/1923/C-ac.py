t=int(input())
for _ in range(t):
    #n=int(input())
    n,q=map(int, input().split())
    #s=input()
    a=list(map(int, input().split()))
    p=[0]
    for i in range(n):
        p.append(p[-1]+a[i])        
    ones=[0]
    for i in range(n):
        ones.append(ones[-1]+(a[i]==1))
    for i in range(q):
        l,r=map(int,input().split())
        if l==r:
            print("NO")
        else:
            o1=ones[r]-ones[l-1]
            ss=p[r]-p[l-1]
            if ss-o1>=r-l+1:
                print("YES")
            else:
                print("NO")