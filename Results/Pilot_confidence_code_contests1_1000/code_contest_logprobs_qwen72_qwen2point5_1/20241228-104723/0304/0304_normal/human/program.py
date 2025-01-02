from __future__ import division
"""x1,y1=map(int,raw_input().split())
x2,y2=map(int,raw_input().split())
n=int(input())
d={"U":(0,1),"D":(0,-1),"R":(1,0),"L":(-1,0)}
di=[(0,0)]
def f(a,b):
    return (a[0]+b[0],a[1]+b[1])
for k in raw_input():
    di.append(f(di[-1],d[k]))"""
N=1001
l=[0]*N
n=int(input())
for k in map(int,raw_input().split()):
    l[k]+=1
if n%2:
    r=[0]*4
    for k in l:
        r[k%4]+=1
    if r[1]+r[3]>1:
        print("NO")
    else:
        ma=[[0]*n for k in range(n)]
        for a,b in enumerate(l):
            if b%2:
                ma[n//2][n//2]=a
        r[0]+=r[1]
        r[2]+=r[3]
        l=[k-k%2 for k in l]
        if r[2]>=n:
            print("NO")
        else:
            print("YES")
            mi=[a for a,b in enumerate(l) if b%4]
            li=[]
            for a,b in enumerate(l):
                li+=[a]*(b//4)
            while len(mi)<n-1:
                mi.append(li[-1])
                mi.append(li[-1])
                li.pop()
            for x in range(n//2):
                ma[n//2][x]=mi[-1]
                ma[n//2][n-1-x]=mi[-1]
                mi.pop()
                ma[x][n//2]=mi[-1]
                ma[n-1-x][n//2]=mi[-1]
                mi.pop()
            for x in range(n//2):
                for y in range(n//2):
                    ma[x][y]=li[-1]
                    ma[n-1-x][y]=li[-1]
                    ma[x][n-1-y]=li[-1]
                    ma[n-1-x][n-1-y]=li[-1]
                    li.pop()
            print("\n".join(map(lambda x:" ".join(map(str,x)),ma)))       
else:
    if max(k%4 for k in l):
        print("NO")
    else:
        print("YES")
        li=[]
        ma=[[0]*n for k in range(n)]
        for a,b in enumerate(l):
            li+=[a]*(b//4)
        for x in range(n//2):
            for y in range(n//2):
                ma[x][y]=li[-1]
                ma[n-1-x][y]=li[-1]
                ma[x][n-1-y]=li[-1]
                ma[n-1-x][n-1-y]=li[-1]
                li.pop()
        print("\n".join(map(lambda x:" ".join(map(str,x)),ma)))
