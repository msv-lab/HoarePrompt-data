N = int(input())

# Calculate the minimal number of layers
layers = (N*(N+1)*(2*N+1)) // 6

# Output the result
print(layers)