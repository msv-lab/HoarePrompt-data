n,q=map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
c=list(map(int, input().split()))
acopy=a.copy()
bcopy=b.copy()
ccopy=c.copy()
# def winefn(ni,ai,bi,ci):
#     wine=0
#     for i in range(ni):
#         wine+=(min(ai[i],bi[i]))
#         ai[i]=ai[i]-(min(ai[i],bi[i]))
#         if i!=ni-1:
#             ai[i+1]=ai[i+1]+min(ai[i],ci[i])
#             ai[i]=ai[i]-min(ai[i],ci[i])
#     return wine

for i in range(q):
    w=0
    a=acopy.copy()
    b=bcopy.copy()
    c=ccopy.copy()
    p,ap,bp,cp=map(int, input().split())
    a[p-1]=ap
    b[p-1]=bp
    acopy[p-1]=ap
    bcopy[p-1]=bp
#     w+=(winefn(n,a,b,c))
#     print(w)
    red=0
    for i in range(n-1):
        if c[i]<(a[i]-min(a[i],b[i])):
            red+=(c[i]-a[i])
    print(min(sum(a),sum(b))-red)