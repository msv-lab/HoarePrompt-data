import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    x=input().rstrip()
    #n,m,k=list(map(int,input().split()))
    l=list(input().split())
    #q=list(map(int,input().split()))
    s=[]
    d=[]
    c=[]
    h=[]
    for i in range(2*n):
        if l[i][1]=='S':
            s.append(l[i])
        elif l[i][1]=='D':
            d.append(l[i])
        elif l[i][1]=='C':
            c.append(l[i])
        else:
            h.append(l[i])
    if x=='S':
        y=s
        w=d
        t=c
        z=h
    elif x=='C':
        y=c
        w=d
        t=s
        z=h
    elif x=='D':
        y=d
        w=s
        t=c
        z=h
    else:
        y=h
        w=d
        t=c
        z=s
    if len(w)%2+len(t)%2+len(z)%2>len(y):
        print("IMPOSSIBLE")
    else:
        w.sort()
        t.sort()
        z.sort()
        y.sort()
        for i in range(len(w)//2):
            a=w.pop()
            b=w.pop()
            print(b,a)
        for i in range(len(t)//2):
            a=t.pop()
            b=t.pop()
            print(b,a)
        for i in range(len(z)//2):
            a=z.pop()
            b=z.pop()
            print(b,a)
        if len(w)>0:
            a=y.pop()
            b=w.pop()
            print(b,a)
        if len(t)>0:
            a=y.pop()
            b=t.pop()
            print(b,a)
        if len(z)>0:
            a=y.pop()
            b=z.pop()
            print(b,a)
        for i in range(len(y)//2):
            a=y.pop()
            b=y.pop()
            print(b,a)