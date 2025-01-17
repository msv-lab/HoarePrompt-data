def modular_exponentiation(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def precompute_factorials(max_n, mod):
    fact = [1] * (max_n + 1)
    ifact = [1] * (max_n + 1)
    
    for i in range(2, max_n + 1):
        fact[i] = (fact[i - 1] * i) % mod
    
    ifact[max_n] = modular_exponentiation(fact[max_n], mod - 2, mod)
    for i in range(max_n - 1, 0, -1):
        ifact[i] = (ifact[i + 1] * (i + 1)) % mod
    
    return fact, ifact

def binomial_coefficient(n, k, fact, ifact, mod):
    if k < 0 or k > n:
        return 0
    return (fact[n] * ifact[k] % mod) * ifact[n - k] % mod

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    queries = []
    max_nk = 0
    idx = 1
    
    for _ in range(t):
        n, k, p = map(int, data[idx:idx + 3])
        queries.append((n, k, p))
        max_nk = max(max_nk, n * k)
        idx += 3
    
    # Precompute factorials and inverse factorials for the largest possible value
    fact, ifact = precompute_factorials(max_nk, queries[0][2])
    
    results = []
    for n, k, p in queries:
        total_good_arrays = 0
        for s in range(n + 1):
            sign = -1 if s % 2 else 1
            total_good_arrays = (total_good_arrays + sign * binomial_coefficient(n, s, fact, ifact, p) * modular_exponentiation(k + 1 - s, n, p)) % p
        
        results.append((total_good_arrays + p) % p)
    
    sys.stdout.write("\n".join(map(str, results)) + "\n")