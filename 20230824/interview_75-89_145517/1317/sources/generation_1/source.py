n, m = map(int, input().split())

count = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if (i**2 + j**2) % m == 0:
            count += 1

print(count)