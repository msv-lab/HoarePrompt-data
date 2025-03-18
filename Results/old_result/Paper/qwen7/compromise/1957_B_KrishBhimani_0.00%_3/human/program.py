for _ in range(int(input())):
    l1=input().split()
    n,k=list(map(int,l1))
    arr=[]
    k0=k
    i=0
    while k:
        if(k&1==1):
            arr.append(i)
        k=k>>1
        i+=1
    ans=[]
    # print(sum([]))
    c=0
    for i in (arr):
        if(c==n-1):
            ans.append(k0-sum(ans))
            break
        c+=1
        ans.append(1<<i)
 
    ans+=[0]*(n-len(ans))
    print(*ans)