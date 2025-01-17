import math
t= int(input())

for _ in range(t):
    L= list(map(int,input().split()))
    n=L[0]
    m=L[1]

    count=0
    for b in range(1,m+1):
        LL=1 if b!=1 else 2 
        UL=int((n/(b*b))+1/b)
        if UL>=LL:
            count+=UL-LL+1
        else:
            break
    print(count)