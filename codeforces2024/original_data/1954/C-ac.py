n=int(input())
for _ in range(n):
    a=input()
    b=input()
    if b>=a:
        a,b=b,a
    a=list(a)
    b=list(b)
    if a[0]==b[0]:
        c=0
        for i in range(len(a)):
            if a[i]!=b[i]:
                c=i
                break
        if c==0:
            pass
        else: 
            for i in range(c+1,len(a)):
                if int(a[i])>int(b[i]):
                    a[i],b[i]=b[i],a[i]
    else:
        for i in range(1,len(a)):
            if int(a[i])>int(b[i]):
                a[i],b[i]=b[i],a[i]
    print(''.join(a))
    print(''.join(b))   