import math

# Read input values
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Calculate the sum of the array
sum_A = sum(A)

# Function to compute the greatest common divisor (GCD) of a list
def gcd_of_list(lst):
    gcd_result = lst[0]
    for num in lst[1:]:
        gcd_result = math.gcd(gcd_result, num)
    return gcd_result

# Function to find all divisors of a number
def find_divisors(x):
    divisors = set()
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            divisors.add(i)
            divisors.add(x // i)
    return sorted(divisors, reverse=True)

# Find the GCD of the array
gcd_A = gcd_of_list(A)

# Find all divisors of sum_A
divisors = find_divisors(sum_A)

# Find the maximum divisor that divides all elements of A
for d in divisors:
    if all((a % d == 0) or ((sum_A - a) % d <= K) for a in A):
        print(d)
        break
