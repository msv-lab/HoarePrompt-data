r=lambda : map(int,input().split())
t,=r()
while t:
    t-=1
    r()
    a=-1e9,*r(),2e9
    b=[0,0]
    # print(a)
    for w,x,y,z in zip(a,a[1:],a[2:],a[3:]):
        v=y-x
        b+=b[-2]+v**(v>(x-w)),b[-1]+v**(v>(z-y))
    # print(b,"B")
    u,=r()
    while u:
        u-=1
        c,d=r()
        # print(c,d)
        if c<d:
            print(b[(d-1)*2]-b[(c-1)*2])
        else:
            print(b[(c*2)-1]-b[(d*2)-1])