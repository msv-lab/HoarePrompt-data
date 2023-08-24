import math

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Read the number of queries
Q = int(input())

# Iterate through each query
for _ in range(Q):
    # Read l and r for each query
    l, r = map(int, input().split())

    # Initialize a counter variable
    count = 0

    # Iterate through odd numbers between l and r
    for num in range(l, r+1, 2):
        # Check if both the number and (number+1)/2 are prime
        if is_prime(num) and is_prime((num+1)//2):
            count += 1

    # Print the count
    print(count)