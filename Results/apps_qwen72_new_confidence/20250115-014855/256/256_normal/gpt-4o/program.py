# Read input
n = int(input())
boys = list(map(int, input().split()))
m = int(input())
girls = list(map(int, input().split()))

# Sort the skill levels of boys and girls
boys.sort()
girls.sort()

# Initialize pointers for boys and girls
i, j = 0, 0
pairs = 0

# Use two-pointer technique to find the maximum number of pairs
while i < n and j < m:
    if abs(boys[i] - girls[j]) <= 1:
        pairs += 1
        i += 1
        j += 1
    elif boys[i] < girls[j]:
        i += 1
    else:
        j += 1

# Print the result
print(pairs)
