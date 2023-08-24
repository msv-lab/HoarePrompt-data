n = int(input())
a = list(map(int, input().split()))

# Find the target value that all elements should be equal to
target = sum(a) // n

# Iterate through each element in the array
for i in range(n):
    # Calculate the difference between the current element and the target value
    diff = target - a[i]

    # Check if the difference is odd
    if diff % 2 != 0:
        print(-1)
        exit()

# Print the minimum non-negative integer value D
print(abs(diff // 2))