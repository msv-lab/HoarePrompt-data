n = int(input())
s = input()

# Initialize a counter for the operations
operations = 1

# Iterate through the string, and count the number of changes in character
for i in range(1, n):
    if s[i] != s[i - 1]:
        operations += 1

print(operations)
