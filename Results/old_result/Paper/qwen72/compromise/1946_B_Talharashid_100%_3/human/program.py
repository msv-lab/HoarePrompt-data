import math
for i in range(int(input())):
    n,k=map(int,input().split())
    l=(list(map(int,input().split())))
    #print(l)
    c=0
    maxi=0
    for ele in l:
        if ele<0 and c<=abs(ele):
            maxi=max(c,maxi);c=0
        else:
            c+=ele
            maxi=max(c,maxi)
    maxi=max(c,maxi)
    print(((2**k)*maxi-maxi+sum(l))%1000000007)