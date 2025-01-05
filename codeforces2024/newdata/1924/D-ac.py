def power(a, b, p):
    # This function calculates (a^b) % p using binary exponentiation.
    if a == 0:
        return 0
    res = 1
    a %= p
    while b > 0:
        if b & 1:
            res = (res * a) % p
        b >>= 1
        a = (a * a) % p
    return res

def pre():
    # Precompute factorials and their modular inverses.
    global fact, inv
    fact = [0] * N
    inv = [0] * N
    fact[0] = inv[0] = 1
    for i in range(1, N):
        fact[i] = (fact[i-1] * i) % mod
    for i in range(1, N):
        inv[i] = power(fact[i], mod-2, mod)

def nCr(n, r):
    # Calculate the binomial coefficient nCr % mod.
    if min(n, r) < 0 or r > n:
        return 0
    if n == r:
        return 1
    return (((fact[n] * inv[r]) % mod) * inv[n-r]) % mod

def f(n, m, k):
    # Calculate the number of sequences with a balanced subsequence of length 2*k.
    if k >= min(n, m):
        return nCr(n+m, m)
    return nCr(n+m, k)

N = 4005
mod = 1000000007

pre()  # Precompute factorials and inverses.

t = int(input())  # Number of test cases.
for _ in range(t):
    n, m, k = map(int, input().split())
    # Calculate the result for each test case.
    result = (f(n, m, k) - f(n, m, k-1) + mod) % mod
    print(result)