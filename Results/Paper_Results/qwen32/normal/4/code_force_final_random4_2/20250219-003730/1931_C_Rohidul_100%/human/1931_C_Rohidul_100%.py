for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    le=len(a)
    l,r=0,n-1
    st,end=1,1
    while l<r and a[l]==a[l+1]:l+=1;st+=1
    while r>l and a[r]==a[r-1]:r-=1;end+=1
 
    ans=le-max(st,end)
    if a[0]==a[-1]:ans=max(0,le-(st+end))
    print(ans)