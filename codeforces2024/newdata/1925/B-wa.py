import math

def find_gcd(x,n):
    xl=[]
    ans=0
    for i in range(1,int(math.sqrt(x)+1)):
        if x%i==0 and i not in xl:
            xl.append(i)
            if x//i>2 and (x//i) not in xl:
                xl.append(x//i)
    l=sorted(xl)
    for ll in reversed(l):
        if ans==0:
            if x//ll>=n and ll>ans:
                ans=ll
        else:
            break
    return ans

t=int(input())
for _ in range(t):
    x,n=map(int,input().split())
    ans=find_gcd(x,n)
    print(ans)

