t=int(input())
buffer=[]
for i in range(t):
    n=int(input())
    w=[int(k) for k in input().split()]
    if n>=3:
        q={}
        # zeta=[0 for j in range(n+1)]
        # #print(type(q))
        # for j in range(n):
        #     if zeta[w[j]]==1:
        #         q[w[j]]+=1
        #     else:
        #         q[w[j]]=1
        #     zeta[w[j]]=1
        #     if w[0]==262144 and j==150901:
        #         print(len(q.keys()))
        #         break
        # if w[0]==262144:
        #     print(n) #(eta_ln)
        #     break
        q=[0 for j in range(n+1)]
        for j in range(n):
            q[w[j]]+=1
        eta=[]
        for j in range(n+1):
            if q[j]>0:
                eta.append(j)
        # epsilon=set()
        # q=[0 for j in range(300000)]
        # for j in range(n):
        #     q[w[j]]+=1
        #     epsilon.add(w[j])
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
                if j>1000:
                    break
            print(res)
    else:
        print(0)