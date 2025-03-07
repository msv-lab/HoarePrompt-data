n=int(input())
def fun():
    ma=mi=0
    m=int(input())
    s=input()
    c=d=0
    l=[]
    for j in s:
        c+=1
        if j=='B':
            mi=c
            break
    for j in s[::-1]:
        d+=1
        if j=='B':
            ma=len(s)-d
            break
    return((ma-mi+2))
for i in range(n):
    print(fun())