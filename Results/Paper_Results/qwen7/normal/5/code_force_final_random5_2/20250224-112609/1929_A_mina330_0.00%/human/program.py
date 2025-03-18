ntest=int(input())
for itest in range(0,ntest,1):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    kq=0
    for i in range(0,len(a)//2,1):
        kq=kq+a[len(a)-i-1]-a[i]
    print(kq)