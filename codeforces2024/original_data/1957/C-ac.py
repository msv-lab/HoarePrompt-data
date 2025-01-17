def precompute_factorials(max_n, mod):
    fact=[1]*(max_n+1)
    for i in range(2, max_n+1):
        fact[i]=(fact[i - 1] * i)%mod
    return fact

def mod_inverse(x, mod):
    return pow(x,mod-2,mod)

def comb(n, k, fact, mod):
    if k>n or k<0:
        return 0
    return (((fact[n] * mod_inverse(fact[k], mod))% mod) * (mod_inverse(fact[n - k], mod)))% mod

t=int(input())
M=10**9 + 7
max_n=1000000 
fact=precompute_factorials(max_n,M)

for _ in range(t):
    n,k=map(int,input().split())
    ans=1

    seen=set()
    for _ in range(k):
        r,c=map(int,input().split())
        seen.update([r, c])
    
    new=set()
    for i in range(1, n + 1):
        if i not in seen:
            new.add(i)
    
    ev = len(new) 
    if (ev % 2)==0:
        for p in range(0,ev,2): 
            n_comb=comb(ev,p,fact,M)
            num=fact[ev - p]
            den=fact[(ev - p) // 2]
            r1=(n_comb*num) % M
            r2=mod_inverse(den, M)
            ans=(ans+ (r1*r2) % M)%M
    else:
        for p in range(1,ev,2): 
            n_comb=comb(ev,p,fact,M)
            num=fact[ev - p]
            den=fact[(ev - p) // 2]
            r1=(n_comb*num) % M
            r2=mod_inverse(den, M)
            ans=(ans+ (r1*r2) % M)%M
    print(ans)
