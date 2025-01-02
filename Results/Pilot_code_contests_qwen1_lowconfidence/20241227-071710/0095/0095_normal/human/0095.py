import sys 
input=sys.stdin.readline 
def ok1(curr):
    n=len(curr)
    return all(l[i]>l[i-1] for i in range(1,n))
def ok2(curr):
    n=len(curr)
    return all(l[i]<l[i-1] for i in range(1,n))
for _ in range(int(input())):
    n=int(input())
    l=[int(i) for i in input().split()]
    if ok1(l) or ok2(l):
        print('Yes')
        continue
    #increase then decreasee 
    ind=-1 
    mini=19**10 
    maxi=0 
    pr=0 
    for i in range(n):
        mini=min(mini,l[i])
        maxi=max(maxi,l[i])
        if l[i]<pr:
            ind=i
            break 
        pr+=1 
    f=1 
    if ind==-1:
        print('Yes')
        continue
    mini=l[ind-1]
    for i in range(ind,n):
        l[i]=min(l[i],mini-1)
        mini=min(mini,l[i])
        if l[i]<0 or mini<0:
            f=0 
    print('Yes' if f else 'No')
    
        
    