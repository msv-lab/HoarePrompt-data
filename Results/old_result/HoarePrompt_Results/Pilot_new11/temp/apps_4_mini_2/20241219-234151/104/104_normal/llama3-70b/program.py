n = int(input())
a = list(map(int, input().split()))

max_erase = 0
for i in range(n):
    for j in range(i + 1, n + 1):
        if all(a[k] - a[i] == k - i for k in range(i, j)):
            max_erase = max(max_erase, j - i - 1)

print(max_erase)
