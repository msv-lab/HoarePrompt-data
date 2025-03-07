from collections import defaultdict
 
def default_value():  
    return 0
    
t=int(input())
while(t>0):
    t-=1 
    d=defaultdict(default_value)
    n,m=list(map(int,input().split())) 
    s=input() 
    for i in range(n):
        d[s[i]]=d[s[i]]+1 
    ans=0
    
    for val in d.keys():
        if(d[val]<=m):
            ans=ans+m-d[val]
    print(ans)