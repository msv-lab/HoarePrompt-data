def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def newman_prime(n):
    """Find the nth Newman-Shanks-Williams prime number."""
    if n == 1:
        return 7  # The first NSW prime is 7
    
    # Initialize the count of NSW primes and the current number
    count = 1
    num = 7
    
    while True:
        # Check if the current number is a prime number
        if is_prime(num):
            # Check if the current prime number is congruent to 1 or 5 modulo 6
            if num % 6 in [1, 5]:
                # Increment the count of NSW primes
                count += 1
                
                # If we have found the nth NSW prime, return it
                if count == n:
                    return num
        
        # Move on to the next number
        num += 1
