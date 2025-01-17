tc=int(input())
for _ in range(tc):
    n=int(input())
    a=[1,1,1]
    k=20000
    while(k>0):
        if a[0]+a[1]+a[2]==n:
            break
        a[2]+=1
        if a[2]>=27:
            a[2]=1
            a[1]+=1
        if a[1]>=27:
            a[2]=1
            a[1]=1
            a[0]+=1
    # print(a[0],a[1],a[2])
    print(chr(a[0]+96)+chr(a[1]+96)+chr(a[2]+96))        