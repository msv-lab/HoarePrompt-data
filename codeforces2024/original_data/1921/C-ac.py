t=int(input())
while(t>0):
    n,f,a,b=map(int,input().split())
    l=list(map(int,input().split()))
    intial_val=0
    charge_req=0
    for i in range(n):
        charge_req+=min((l[i]-intial_val)*a,b)
        intial_val=l[i]
    if f-charge_req>0:
        print("YES")
    else:
        print("NO")
    t-=1
        