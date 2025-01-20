n = int(input())
s = input()

# Function to find the minimum number of operations to type the string
def min_operations_to_type(n, s):
    # Initialize the operations count to n (typing each character one by one)
    min_operations = n
    
    # Try to find the optimal place to perform the copy operation
    for i in range(1, n):
        # Find the length of the substring to copy
        if s[:i] == s[i:2*i]:
            # Calculate the number of operations
            operations = i + 1 + (n - 2*i)
            min_operations = min(min_operations, operations)
    
    return min_operations

# Get the result
result = min_operations_to_type(n, s)

# Print the result
print(result)
