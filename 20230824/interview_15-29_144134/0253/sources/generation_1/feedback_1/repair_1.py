k1, k2, k3 = map(int, input().split())

# Function to calculate the greatest common divisor (GCD) using the Euclidean algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to calculate the least common multiple (LCM) using the GCD
def lcm(a, b):
    return a * b // gcd(a, b)

# Calculate the LCM of the given time intervals using the correct formula
lcm_k = lcm(lcm(k1, k2), k3)

# Check if the LCM is greater than the sum of the maximum time interval and the other two time intervals
if lcm_k <= (k1 + k2 + k3):
    print("NO")
else:
    print("YES")