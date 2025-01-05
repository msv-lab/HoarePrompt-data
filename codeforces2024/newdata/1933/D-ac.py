for _ in range(int(input())):
    n=int(input())
    a=sorted(list(map(int,input().split())))
    ans=0

    if a.count(a[0])==1:
        ans=1
    else:
        for i in range(1,n):
            if a[i]%a[0]!=0:
                ans=1
                break
            else:
                continue
        
    if ans==1:
        print("YES")
    else:
        print("NO")