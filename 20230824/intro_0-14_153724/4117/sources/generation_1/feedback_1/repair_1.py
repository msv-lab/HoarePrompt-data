# Read N and the lengths of the sticks
N = int(input())
L = list(map(int, input().split()))

# Initialize the counter for valid triangles
count = 0

# Sort the lengths of the sticks in ascending order
L.sort()

# Initialize a set to store the unique combinations of stick lengths
triangles = set()

# Outer loop through each possible starting stick
for i in range(N-2):
    # Middle loop through each possible second stick
    for j in range(i+1, N-1):
        # Inner loop through each possible third stick
        for k in range(j+1, N):
            # Check if the three sticks can form a triangle
            if L[i] + L[j] > L[k]:
                # Add the unique combination of stick lengths to the set
                triangles.add((L[i], L[j], L[k]))

# Get the count of distinct triangles
count = len(triangles)

# Print the number of ways to choose three sticks that can form a triangle
print(count)