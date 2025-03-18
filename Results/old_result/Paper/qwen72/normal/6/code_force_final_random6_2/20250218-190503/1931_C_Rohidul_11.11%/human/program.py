for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    # le=len(set(a))
    l,r=0,n-1
    st,end=0,0
    while l<r and a[l]==a[l+1]:l+=1;st+=1
    while r>l and a[r]==a[r-1]:r-=1;end+=1
 
    # print(l,r)
 
    if a[0]==a[-1]:ans=r-l-1
    elif st==0 and end==0 and a[0]!=a[-1]:ans=len(a)-1
    else:ans=r-l
    print(max(0,ans))