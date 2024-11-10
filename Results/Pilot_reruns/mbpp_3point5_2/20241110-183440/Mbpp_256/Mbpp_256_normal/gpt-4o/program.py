def count_Primes_nums(n):
    if n <= 2:
        return 0
    
    # Initialize a list to keep track of prime status for each number up to n-1
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False # 0 and 1 are not prime numbers
    
    # Sieve of Eratosthenes
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    
    # Count primes less than n
    return sum(is_prime)

# Test cases
assert count_Primes_nums(5) == 2
assert count_Primes_nums(10) == 4
assert count_Primes_nums(100) == 25
