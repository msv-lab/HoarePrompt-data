def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())

# If n is prime, the solution is the number itself
if is_prime(n):
    print(1)
    print(n)
else:
    # First, check if n - 2 is prime
    if is_prime(n - 2):
        print(2)
        print(2, n - 2)
    else:
        # Loop through all possible prime numbers less than n
        # and check if n - p is prime
        for p in range(3, n, 2):
            if is_prime(p) and is_prime(n - p):
                print(3)
                print(p, n - p)
                break