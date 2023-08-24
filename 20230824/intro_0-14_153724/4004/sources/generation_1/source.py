n = int(input())
a = list(map(int, input().split()))

# Find the minimum and maximum values in the array
min_val = min(a)
max_val = max(a)

# Check if all values are already equal
if min_val == max_val:
    print(0)
    exit()

# Find the target value that all elements should be equal to
target = (min_val + max_val) // 2

# Iterate through each element in the array
for i in range(n):
    # Calculate the difference between the current element and the target value
    diff = target - a[i]

    # Check if the difference is divisible by 2
    if diff % 2 != 0:
        print(-1)
        exit()

# Print the minimum non-negative integer value D
print(diff // 2)