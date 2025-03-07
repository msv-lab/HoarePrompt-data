t=int(input())
buffer=[]
for i in range(t):
    n=int(input())
    w=[int(k) for k in input().split()]
    if n>=3:
        q=[0 for j in range(n+1)]
        for j in range(n):
            q[w[j]]+=1
        eta=[]
        for j in range(n+1):
            if q[j]>0:
                eta.append(j)
        eta_ln=len(eta)
        rho=q[eta[0]]
        if eta_ln==1:
            print(n*(n-1)*(n-2)//6)
        else:
            res=q[eta[0]]*(q[eta[0]]-1)*(q[eta[0]]-2)//6
            for j in range(1, eta_ln):
                res+=q[eta[j]]*(q[eta[j]]-1)*(q[eta[j]]-2)//6
                res+=q[eta[j]]*(q[eta[j]]-1)//2*rho
                rho+=q[eta[j]]
            print(res)
    else:
        print(0)