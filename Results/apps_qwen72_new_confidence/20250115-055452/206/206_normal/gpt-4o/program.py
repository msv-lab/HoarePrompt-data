def prime_factors(b):
    """ Return the prime factors of b as a dictionary where keys are the prime factors and values are their powers """
    factors = {}
    d = 2
    while b > 1:
        while (b % d) == 0:
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
            b //= d
        d += 1
        if d * d > b:
            if b > 1:
                if b in factors:
                    factors[b] += 1
                else:
                    factors[b] = 1
            break
    return factors

def count_factors(n, p):
    """ Return the number of times prime p is a factor in n! """
    count = 0
    power = p
    while power <= n:
        count += n // power
        power *= p
    return count

def trailing_zeros_in_base_factorial(n, b):
    """ Calculate the number of trailing zero digits in the b-ary representation of n! """
    factors = prime_factors(b)
    min_zeros = float('inf')
    
    for prime, power in factors.items():
        count = count_factors(n, prime) // power
        if count < min_zeros:
            min_zeros = count
    
    return min_zeros

# Reading input
import sys
input = sys.stdin.read
data = input().strip().split()
n = int(data[0])
b = int(data[1])

# Calculating the result
result = trailing_zeros_in_base_factorial(n, b)

# Printing the result
print(result)
