def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def solve(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            for k in range(j, len(primes)):
                if primes[i] + primes[j] + primes[k] == n:
                    return primes[i], primes[j], primes[k]
    return None

n = int(input())
result = solve(n)

print(3)
print(result[0], result[1], result[2])