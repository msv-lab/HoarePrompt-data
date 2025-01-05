mod = int(1e9+7)

fac = [1]

def add(a, b):
    c = a + b
    if c >= mod:
        c -= mod
    return c

def subtract(a, b):
    return (a - b) % mod

def mul(a, b):
    return (a * b) % mod

def my_pow(a, b):
    if b == 0:
        return 1
    if b % 2 == 1:
        return mul(a, my_pow(a, b-1))
    else:
        temp = my_pow(a, b/2)
        return temp * temp
    
def my_inv(a):
    return my_pow(a, mod-2)

def nCk(n, k, fac):
    if k > n:
        return 0
    #print(fac[n])
    #print(my_inv(mul(fac[n-k], fac[k])))
    return mul(fac[n], my_inv(mul(fac[n-k], fac[k])))

def main():
    n, k = [int(x) for x in raw_input().split()]
    
    a = [int(x) for x in raw_input().split()]
    
    fac = [0] * (n+5)
    
    #print(fac)
    
    fac[0] = 1
    
    for i in range(1, n+5):
        fac[i] = mul(fac[i-1], i)
    
    a.sort()
    
    ans = 0
    
    for i in range(n-1):
        #print(a[i])
        diff = subtract(a[i+1], a[i])
        ways = nCk(n, k, fac)
        #print(ways)
        ways = subtract(ways, nCk(i+1, k, fac))
        ways = subtract(ways, nCk(n-i-1, k, fac))
        ans = add(ans, mul(diff, ways))
    
    print(ans)
    

main()