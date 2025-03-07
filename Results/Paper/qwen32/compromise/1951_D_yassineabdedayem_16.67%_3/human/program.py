from sys import stdin
t=int(input())
for _ in range(t):
    n,k=map(int,stdin.readline().split())
    rep=0
    number=0
    tab=[]
    while n!=0 and k>0 and rep<60 and n>=k:
        
        Min,Max=min(n//k,k),max(int(n/k),k)
        if Max==k and n*Min<=k:
            number=Min
            k=k-Max
        else:
            number=Max
            k=k-Min
        tab.append(str(number))
        n-=Min*Max
        rep+=1
    if k==0:
        print("YES")
        print(len(tab))
        for i in tab:
            print(i,end=" ")
    else:
        print("NO")