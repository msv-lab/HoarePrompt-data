def gc(a,b):
    while b:
        a,b=b,a%b
    return abs(a)
dire={}
def f(a,b):
    x0,y0=a
    x1,y1=b
    dx=x1-x0
    dy=y1-y0
    d=gc(dx,dy)
    dx//=d
    dy//=d
    if dy<0:
        dy*=-1
        dx*=-1
    if dy==0:
        dx=1
    if dx==0:
        dy=1
    #croise x=0 en y0-dy*x0/dx
    cl=(dx,dy)
    if dx:
        n1=y0*dx-dy*x0
        d1=dx
        d=gc(n1,d1)
        n1//=d
        d1//=d
        if d1<0:
            d1*=-1
            n1*=-1
        v=(n1,d1)
    else:
        v=x0
    if not(cl in dire):
        dire[cl]={v}
    else:
        dire[cl].add(v)
n=int(input())
l=[]
for k in range(n):
    l.append(tuple(map(int,raw_input().split())))
for k in range(n):
    for i in l[k+1:]:
        f(l[k],i)
dire=[len(dire[k]) for k in dire]
s=sum(dire)
print(sum((s-k)*k for k in dire)//2)
