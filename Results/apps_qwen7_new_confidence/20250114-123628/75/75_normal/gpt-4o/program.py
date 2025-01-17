def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    p = 2
    while p * p <= limit:
        if sieve[p]:
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
        p += 1
    primes = [p for p, is_prime in enumerate(sieve) if is_prime]
    return primes

def find_three_prime_sum(n):
    if is_prime(n):
        return (1, [n])
    if is_prime(n - 2):
        return (2, [2, n - 2])
    
    limit = 10**6
    primes = find_primes(limit)
    prime_set = set(primes)

    for i in primes:
        for j in primes:
            if i + j >= n:
                break
            if (n - i - j) in prime_set:
                return (3, [i, j, n - i - j])
    return None

import sys
input = sys.stdin.read
n = int(input().strip())

result = find_three_prime_sum(n)
if result:
    k, primes = result
    print(k)
    print(" ".join(map(str, primes)))
else:
    print(-1)
