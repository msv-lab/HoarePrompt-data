import collections
for _ in range(int(input())):
    n,m = map(int,input().split())
    print("?",1,1)
    x = int(input())
    print("?",x+1,1)
    x1 = int(input())
    print("?",1,1+x)
    x2 = int(input())
    if x1%2==1:
        p = [1,x+1]
        while x2>0:
            p = [p[0]+1,p[1]-1]
            x2-=2
    elif x2%2==1:
        p = [1+x,1]
        while x1>0:
            p = [p[0]-1,p[1]+1]
            x1-=2
    else:
        p = [1+x,1]
        while x1>0:
            p = [p[0]-1,p[1]+1]
            x1-=2
        print("?",*p)
        i = int(input())
        if i!=0:
            p = [1,x+1]
            while x2>0:
                p = [p[0]+1,p[1]-1]
                x2-=2
    print("!",*p)