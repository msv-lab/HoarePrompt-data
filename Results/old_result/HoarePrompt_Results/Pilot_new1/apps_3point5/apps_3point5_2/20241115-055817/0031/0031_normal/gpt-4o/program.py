import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve(n, k):
    MOD = 10**6 + 3
    
    if k > (1 << n):
        print(1, 1)
        return
    
    total_days = 1 << n
    
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator = numerator * (total_days - i) % MOD
        denominator = denominator * total_days % MOD
    
    p_no_shared = numerator
    p_total = denominator
    
    p_shared = (p_total - p_no_shared + MOD) % MOD
    
    A = p_shared
    B = p_total
    
    g = gcd(A, B)
    A //= g
    B //= g
    
    print(A % MOD, B % MOD)

# Read input
n, k = map(int, input().split())
solve(n, k)
