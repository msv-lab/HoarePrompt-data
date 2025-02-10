from math import sqrt
for q in range(int(input())):
    x,n=list(map(int,input().split(' ')))
    ans=1
    for i in range(1,int(sqrt(x))+1):
        if(x%i==0):
            if((x-n*i)>=0 and (x-n*i)%i==0):
                ans=max(ans,i)
            if((x-n*((x//i))>=0 and x//i>0 and (x-n*((x//i))%((x//i))==0))):
                ans=max(ans,(x//i))
    print(ans)