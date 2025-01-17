n, m = map(int, input().split())

# Count group sizes based on remainder when divided by 5
group_n = [0] * 5
group_m = [0] * 5

for i in range(1, n + 1):
    group_n[i % 5] += 1

for i in range(1, m + 1):
    group_m[i % 5] += 1

# Calculate the number of valid pairs
result = (group_n[0] * group_m[0] +
          group_n[1] * group_m[4] +
          group_n[2] * group_m[3] +
          group_n[3] * group_m[2] +
          group_n[4] * group_m[1])

print(result)
