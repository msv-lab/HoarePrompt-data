
import sys
#sys.stdin=open("data.txt")
input=sys.stdin.readline


n,k=map(int,input().split())
a,b,c,d=map(int,input().split())

if n==4:
    # special case
    print("-1")
elif k>=n+1:
    # i know that having n+1 roads is possible
    # assume n>=5
    # get the chain
    chain=[a,c]
    for i in range(1,n+1):
        if i not in [a,b,c,d]:
            chain.append(i)
    chain.append(b)
    chain.append(d)
    # print first path
    p1=list(chain)
    p1[-1],p1[-2]=p1[-2],p1[-1]
    print(" ".join(map(str,p1)))
    # print second path
    p2=list(chain)
    p2[0],p2[1]=p2[1],p2[0]
    print(" ".join(map(str,p2)))
else:
    print("-1")