# Read the input N
N = int(input())

# Read the input sequence B
B = list(map(int, input().split()))

# Initialize the maximum sum as the sum of the last two elements of B
max_sum = B[-1] + B[-2]

# Iterate over the elements of B in reverse order
for i in range(N-3, -1, -1):
    # Find the maximum value between the current element of B and the next element of B
    max_value = max(B[i], B[i+1])
    # Update the maximum sum by adding the maximum value
    max_sum += max_value

# Print the maximum sum
print(max_sum)