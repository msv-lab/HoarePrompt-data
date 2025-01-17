n=int(input())
for _ in range(n):
    a=input()
    b=input()
    if b>=a:
        a,b=b,a
    a=list(a)
    b=list(b)
    if a[0]==b[0]:
        for i in range(2,len(a)):
            if int(a[i])>int(b[i]):
                a[i],b[i]=b[i],a[i]
    else:
        for i in range(1,len(a)):
            if int(a[i])>int(b[i]):
                a[i],b[i]=b[i],a[i]
    print(''.join(a))
    print(''.join(b))