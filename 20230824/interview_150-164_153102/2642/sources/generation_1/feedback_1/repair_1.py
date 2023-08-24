mod = 1000000007

n = int(input())
sardines = []
for _ in range(n):
    a, b = map(int, input().split())
    sardines.append((a, b))

count = 0
for i in range(n):
    for j in range(i+1, n):
        # Check if two sardines are on bad terms
        if (sardines[i][0] * sardines[j][0] + sardines[i][1] * sardines[j][1]) != 0:
            count += 1

# Add one for each individual sardine
count += n

# Take modulo
count %= mod

print(count)