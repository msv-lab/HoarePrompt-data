n,x=map(int,raw_input().split())
if n==2 and x==2:
    print("Yes")
    print(1)
    print(2)
    print(3)
    exit()
elif n==2 and x!=2:
    print("No")
    exit()
ans=[0]*(2*n-1)
if x-2>=1 and x+2<=2*n-1:
    print("Yes")
    ans[(2*n-1)/2]=x
    ans[(2*n-1)/2+1]=x+1
    ans[(2*n-1)/2-1]=x-1
    ans[(2*n-1)/2+2]=x-2
    ans[(2*n-1)/2-2]=x+2
    j=1
    i=0
    while i<2*n-1:
        if j==x or j==x-1 or j==x+1 or j==x+2 or j==x-2:
            j+=1
            continue
        if ans[i]!=0:
            i+=1
            continue
        else:
            ans[i]=j
            j+=1
            i+=1
    for i in xrange(2*n-1):
        print(ans[i])
else:
    print("No")