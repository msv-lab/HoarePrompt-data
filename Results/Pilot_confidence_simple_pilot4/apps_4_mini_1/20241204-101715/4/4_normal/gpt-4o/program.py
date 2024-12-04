def max_painted_sections(n, q, painters):
    max_painted = 0

    # Initially paint with all painters
    painted = [0] * (n + 1)
    for l, r in painters:
        for i in range(l, r + 1):
            painted[i] += 1

    total_painted = sum(1 for p in painted if p > 0)

    # Try removing each pair of painters and calculate the number of painted sections
    for i in range(q):
        for j in range(i + 1, q):
            temp_painted = painted[:]
            for k in range(painters[i][0], painters[i][1] + 1):
                temp_painted[k] -= 1
            for k in range(painters[j][0], painters[j][1] + 1):
                temp_painted[k] -= 1
            current_painted = sum(1 for p in temp_painted if p > 0)
            max_painted = max(max_painted, current_painted)

    return max_painted

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
q = int(data[1])
painters = []

for i in range(q):
    l = int(data[2 + 2*i])
    r = int(data[3 + 2*i])
    painters.append((l, r))

print(max_painted_sections(n, q, painters))
