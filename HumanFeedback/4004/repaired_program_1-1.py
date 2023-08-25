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
target = 0
for i in range(n):
    target += a[i]

# Check if the target value is divisible by n
if target % n != 0:
    print(-1)
    exit()

# Calculate the value that all elements should be equal to
target //= n

# Find the minimum non-negative integer value of D
D = max(target - min_val, max_val - target)

print(D)