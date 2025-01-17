t=int(input())

for _ in range(t):
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    a_original=a
    
    if k>=m:
        elements=k//m
        if (k%m)!=0:
            elements+=1
    else:
        elements=1
    #print(elements)    

    ko=k-m*(elements-1)
    a.sort()
    maxi=a[elements-1]
    nl=[]
    
    pind=-1
    for rr in range(n):
        if a_original[rr]<=maxi:
            pind+=1
            if pind==elements:
                break
            nl.append(a_original[rr])
            

            if a_original[rr]==maxi:
                perfect_index=pind

    price=0
    f=0
    for j in range(len(nl)):
        if nl[j]==maxi and j==perfect_index:
            price+=(nl[j]+f)*ko
            #print(price,88)
            f+=ko
        else:
            price+=(nl[j]+f)*m
            #print(price,69)
            f+=m   

    print(price)  