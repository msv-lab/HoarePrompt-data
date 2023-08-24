import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def solve(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            for k in range(j+1, len(primes)):
                if primes[i] + primes[j] + primes[k] == n:
                    return primes[i], primes[j], primes[k]
    return None

n = int(input())
result = solve(n)

if result is None:
    print("No solution")
else:
    print(3)
    print(result[0], result[1], result[2])