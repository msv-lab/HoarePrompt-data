for _ in range(int(input())):
    x,n=map(int,input().split())
    ans=1
    for i in range(1,int(x**(0.5))+1):
        if(x%i==0):
            if(n<=x//i):ans=max(ans,i)
            if(n<=i):ans=max(ans,x//i)
    print(ans)