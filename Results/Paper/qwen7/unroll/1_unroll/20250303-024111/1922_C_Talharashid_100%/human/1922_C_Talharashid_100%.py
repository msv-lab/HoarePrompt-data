from collections import defaultdict
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    d1=defaultdict(int)
    d2=defaultdict(int)
    d1[2]=1
    for i in range(1,n-1):
        if (l[i+1]-l[i])<(l[i]-l[i-1]) :
            d1[i+2]=1+d1[i+1]
        else:
            d1[i+2]=(l[i+1]-l[i])+d1[i+1]
    d2[n-1]=1
    for i in range(n-2,0,-1):
        if (l[i]-l[i-1])<(l[i+1]-l[i]) :
            d2[i]=1+d2[i+1]
        else:
            d2[i]=(l[i]-l[i-1])+d2[i+1]
    #print(d1,d2)
    m=int(input())
    for j in range(m):
        x,y=(map(int,input().split()))
        if y>x:
            print(d1[y]-d1[x])
        else:
            print(d2[y]-d2[x])