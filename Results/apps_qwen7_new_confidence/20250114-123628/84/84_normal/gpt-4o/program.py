import math

# Read input
n = int(input())
a = list(map(int, input().split()))

# Function to check if a given d satisfies the condition
def is_valid_d(d):
    positive_count = sum(1 for x in a if x / d > 0)
    return positive_count >= math.ceil(n / 2)

# Iterate over possible values of d and check if they satisfy the condition
for d in range(1, 1001):
    if is_valid_d(d):
        print(d)
        exit()

for d in range(-1, -1001, -1):
    if is_valid_d(d):
        print(d)
        exit()

# If no valid d is found, print 0
print(0)
