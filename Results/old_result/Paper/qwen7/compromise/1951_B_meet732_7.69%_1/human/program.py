def mwins(a):
    x=a[k]
 
    ind=[]
    c=0
    for i in range(n):
        if a[i]>x:
            ind.append(i)
            c+=1
        if c==2:break
    if k==14:print(ind)
    if ind==[]:return n-1
    if len(ind)==1:
        if ind[0]==0:
            return k-1
        if ind[0]>k:return ind[0]-1
        return max(k-ind[0],ind[0]-1)
    if ind[0]==0: return min(ind[1]-1,k-1)
    if k>ind[1]: return max(ind[0]-1,ind[1]-ind[0])
    return max(ind[0]-1,k-ind[0])
    
 
 
 
for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    k-=1
    print(mwins(l))