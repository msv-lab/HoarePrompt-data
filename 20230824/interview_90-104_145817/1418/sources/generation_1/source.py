# Read input
n = int(input())

# Initialize list to store the values of a_i
a = [0] * (n-1)

# Assign values to a_i
for i in range(2, n+1):
    # Set the initial value as 1
    a[i-2] = 1
    
    # Check if i is a prime number
    is_prime = True
    for j in range(2, int(i**(1/2))+1):
        if i % j == 0:
            is_prime = False
            break
    
    # If i is prime, assign it a unique value
    if is_prime:
        a[i-2] = i

# Print the values of a_i
print(" ".join(str(x) for x in a))