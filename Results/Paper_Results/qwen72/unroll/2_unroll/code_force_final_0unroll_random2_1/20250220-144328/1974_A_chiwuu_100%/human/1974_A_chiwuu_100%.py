n=int(input())
for i in range(n):
    a,b=input().split()
    a=int(a)
    b=int(b)
    t=b
    if t%2==0:
        t=t//2
    else:
        t=t//2+1
    t1=t*15-b*4
    if t1>=a:
        t=t
    else:
        t2=a-t1
        if t2%15==0:
            t=t+t2//15
        else:
            t=t+t2//15+1
    print(t)