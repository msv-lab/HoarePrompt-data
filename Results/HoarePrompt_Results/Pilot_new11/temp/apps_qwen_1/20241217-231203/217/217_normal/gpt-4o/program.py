# Read the input values
n = int(input())
a = list(map(int, input().split()))

# Calculate the maximum possible value of B - C
# To maximize B - C, we should include all positive numbers in B and all negative numbers in C
B = sum(x for x in a if x > 0)
C = sum(x for x in a if x < 0)

# The maximum value of B - C
result = B - C

# Print the result
print(result)
