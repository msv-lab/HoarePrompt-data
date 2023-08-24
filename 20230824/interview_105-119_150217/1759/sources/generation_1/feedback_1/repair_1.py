m, n = map(int, input().split())
pictures = []
for _ in range(m):
    picture = list(map(int, input().split()))
    pictures.append(picture)

results = []
for i in range(m):
    time = 0
    for j in range(n):
        time += pictures[i][j]
    results.append(time)

for i in range(1, m):
    results[i] += results[i-1]

print(' '.join(map(str, results)))