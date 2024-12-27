n=input()
a=map(int,raw_input().split())
mod=998244353
a.sort()
firsum=0
secsum=0
for i in range(len(a)):
    if i<n:
        firsum+=a[i]
    else:
        secsum+=a[i]
k=abs(secsum-firsum)%mod
fac=[1,1]
for i in range(2,2*n+1):
    fac.append((fac[-1]*i)%mod)
rr=(fac[n]**2)%mod
g=pow(rr,mod-2,mod)
print ((k*((fac[2*n]*g)%mod))%mod)