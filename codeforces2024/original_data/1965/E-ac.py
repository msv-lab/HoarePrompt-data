n, m, k = map(int, input().split())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

ans = []

for x in range(n):
    for y in range(m):
        for z in range(1, n + 1):
            if y % 2 == 1:
                ans.append([x, y, z, a[x][y]])
            else:
                ans.append([x, y, z, a[min(x, n - z)][y]])
        for z in range(n + 1, n + k + 1):
            if y % 2 == 1:
                ans.append([x, y, z, a[x][y]])
            else:
                ans.append([x, y, z, z - n])

for x in range(n, n + k):
    for y in range(m):
        for z in range(1, n + 1):
            if y % 2 == 1:
                ans.append([x, y, z, x - n + 1])
            else:
                ans.append([x, y, z, a[n - z][y]])
        ans.append([x, y, n + 1, x - n + 1])

for y in range(m):
    for z in range(n + 2, n + k + 1):
        ans.append([n, y, z, z - n])

for x in range(n + 1, n + k):
    for z in range(n + 2, n + k + 1):
        ans.append([x, 0, z, max(x - n + 1, z - n)])

print(len(ans))

for cube in ans:
    print(cube[0] + 1, cube[1] + 1, cube[2] + 1, cube[3])