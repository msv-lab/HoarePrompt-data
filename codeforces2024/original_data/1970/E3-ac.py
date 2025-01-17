mod = 10**9+7
m, n = map(int, input().split())
k0 = list(map(int, input().split()))
k1 = list(map(int, input().split()))
assert len(k0)==len(k1)==m
 
c00 = sum(a*a for a in k0) % mod
c11 = sum(a*a for a in k1) % mod
c01 = sum(a*b for a,b in zip(k0,k1)) % mod
 
m00 = (c00+c01) % mod
m01 = (c01+c11) % mod
m10 = c00
m11 = c01
m = m00,m01,m10,m11
 
def matmul(a, b):
    a00,a01,a10,a11 = a
    b00,b01,b10,b11 = b
    c00 = a00*b00 + a01*b10
    c01 = a00*b01 + a01*b11
    c10 = a10*b00 + a11*b10
    c11 = a10*b01 + a11*b11
    return c00%mod, c01%mod, c10%mod, c11%mod
    
def matpow(a, n):
    if n==0:
        return 1,0,0,1
    if n==1:
        return a
    n2, r  = divmod(n,2)
    an2 = matpow(a, n2)
    an = matmul(an2, an2)
    if r:
        an = matmul(an, a)
    return an
 
mn00,mn01,mn10,mn11 = matpow(m, n-1)
u0 = k0[0]*mn00 + k1[0]*mn10
u1 = k0[0]*mn01 + k1[0]*mn11
 
res = ((u0+u1)*sum(k0) + u0*sum(k1)) % mod
print(res)