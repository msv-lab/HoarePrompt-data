n = int(input())
a = list(map(int, input().split()))

max_erase = 0

for i in range(1, n):
    max_erase = max(max_erase, a[i] - a[i-1] - 1)

print(max_erase)
