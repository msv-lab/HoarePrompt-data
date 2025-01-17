from collections import Counter
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    #n=int(input())
    n,m,k=list(map(int,input().split()))
    #p=list(map(int,input().split()))
    #q=list(map(int,input().split()))
    a=list(input().split())
    b=list(input().split())
    d={}
    cna=Counter()
    cnb=Counter()
    c=0
    g=0
    for i in range(m):
        cnb[b[i]]+=1
    for i in range(m):
        cna[a[i]]+=1
    for i in cna:
        if cna[i]!=0 and cnb[i]!=0:
            c+=min(cna[i],cnb[i])
    if c>=k:
        g+=1
            
    for i in range(1,n-m+1):
        c-=min(cna[a[i-1]],cnb[a[i-1]])
        cna[a[i-1]]-=1
        c+=min(cna[a[i-1]],cnb[a[i-1]])
        
        c-=min(cna[a[i+m-1]],cnb[a[i+m-1]])
        cna[a[i+m-1]]+=1
        c+=min(cna[a[i+m-1]],cnb[a[i+m-1]])
        
        if c>=k:
            g+=1
    print(g)